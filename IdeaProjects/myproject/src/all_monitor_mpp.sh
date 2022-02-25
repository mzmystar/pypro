#!/bin/ksh

. $HOME/.profile
. /code/crm/crmbm/work/interChk/monitor/all_monitor/all_monitor_com.sh

run_ora_sql() {

  ORACLEID="aigh/Cfr43qa1@SHBASS1"
  SQL=$1

  ReturnData=$(echo "$SQL;" | sqlplus -s $ORACLEID)
  Orastr=$?
  if [ ${Orastr} -ne 0 ]; then
    Write_Log_File "oracle SQL错误,Error Msg: ${ReturnData}"
    exit -1
  fi

  ReturnStr=$(echo "${ReturnData}" | sed -e '4,/^$/!d;/^$/d' | sed 's/ //g')
}

ora_exp() {
  SQL=$1
  tmp_file=$2
  sqlplus -s mds/1zhxcqL_@BASS2 <<eof
set echo off;
set feedback off;
set linesize 2500;
set pagesize 0;
set heading off;
set term off;
set termout off;
set trimspool on;
set trimout on;
spool $tmp_file
$SQL;
spool off
exit
eof
}

#写日志文件
Write_Log_File() {
  now_time=$(date +"%Y-%m-%d %H:%M:%S")
  echo "${now_time} 写日志文件：${1}"
  echo "${now_time} ${1}" >>${Log_File}
}

check_mpp() {
  cp ${PATH_LOG}/mpp_proc_fail.tmp ${PATH_LOG}/mpp_proc_fail_lastone.tmp
  rm -f ${PATH_LOG}/mpp_proc_fail.tmp
  rm -f ${PATH_LOG}/proc_fail_sql.txt
  ora_exp "select * from mpp_proc_fail" "${PATH_LOG}/mpp_proc_fail.tmp"
  fail_cnt=$(cat ${PATH_LOG}/mpp_proc_fail.tmp | wc -l)
  HHMM=$(echo $(date) | awk '{print $4}' | cut -c1-5)
  ${connmpp}
  cat ${PATH_LOG}/mpp_proc_fail.tmp | sed 's/\"//g' | while read line; do
    run_platform=$(echo ${line} | awk '{print $1}')
    groupname=$(echo ${line} | awk '{print $2}')
    proc_name=$(echo ${line} | awk '{print $3}')
    end_time=$(echo ${line} | awk '{print $4}')
    log_time=$(echo $end_time | sed 's/\-//g')
    mm=$(echo ${line} | awk '{print $5}')
    msg=$(cat /expfile/dacp/pst-proc-1.0.0-SNAPSHOT/logs/${log_time}/${proc_name}.log | grep "DB2 SQL error" | tail -1 | awk -F 'DB2 SQL error:' '{print $NF}')

    if [ -n "${msg}" ]; then
      SQLCODE=$(echo ${msg} | awk -F"," '{print $1}' | awk -F":" '{print $2}')
      SQLSTATE=$(echo ${msg} | awk -F"," '{print $2}' | awk -F":" '{print $2}')
      SQLERRMC=$(echo ${msg} | awk -F"," '{print $3}' | awk -F":" '{print $2}')
    else
      SQLCODE="未找到"
      SQLSTATE="未找到"
      SQLERRMC="未找到日志"
    fi
    #新增连数据库查表功能
    SQLCODE=$(echo ${SQLCODE} | sed 's/ //g')
    if [ "${SQLCODE}" == "-204" ]; then
      #Write_Log_File "sqlcode为${SQLCODE}"

      db2_num=$(db2 -x "select count(1) from syscat.tables where trim(tabschema)||'.'||trim(tabname)=trim('${SQLERRMC}')")
      #Write_Log_File "select count(1) from syscat.tables where trim(tabschema)||'.'||trim(tabname)='${SQLERRMC}'"
      #Write_Log_File "db2库查询表数量${db2_num}"
      db2_num=$(echo ${db2_num} | sed 's/ //g')
      if [ ${db2_num} -gt 0 ]; then
        SQLERRMC="${SQLERRMC},现有表"
      fi
    fi

    echo "insert into db2info.proc_fail_log values('${groupname}','${proc_name}','${end_time}','${SQLCODE}','${SQLSTATE}','${SQLERRMC}','${mm}','${run_platform}');" >>${PATH_LOG}/proc_fail_sql.txt
  done
  diff ${PATH_LOG}/mpp_proc_fail.tmp ${PATH_LOG}/mpp_proc_fail_lastone.tmp >/dev/null
  if [ $? -eq 0 ]; then
    Write_Log_File "检查mp挂起与上一次内容相同"
  else
    #${connmpp}
    db2 "delete from db2info.proc_fail_log where run_platform='DIM_RUN_PLATFORM_T002'"
    db2 -tvf ${PATH_LOG}/proc_fail_sql.txt
    Write_Log_File "mp挂起信息更新"
    db2 connect reset
  fi
}

check_yt() {
  cp ${PATH_LOG}/yt_proc_fail.tmp ${PATH_LOG}/yt_proc_lastone_fail.tmp
  rm -f ${PATH_LOG}/proc_fail_yt_sql.txt
  rm -f ${PATH_LOG}/yt_proc_fail.tmp
  rm -f ${PATH_LOG}/proc_bad_sql.tmp
  #去94库查YT机挂起程序

  ora_exp "select * from yt_proc_fail" "${PATH_LOG}/yt_proc_fail.tmp"
  cat ${PATH_LOG}/yt_proc_fail.tmp | sed 's/\"//g' | while read line; do
#    单行处理
    run_platform=$(echo ${line} | awk '{print $1}')
    groupname=$(echo ${line} | awk '{print $2}')
    proc_name=$(echo ${line} | awk '{print $3}')
    end_time=$(echo ${line} | awk '{print $4}')
    mm=$(echo ${line} | awk '{print $5}')
    #log_time=`echo ${end_time}" "${mm}`
    log_time=$(echo $end_time | sed 's/\-//g')
    #将挂起程序去94库查报错语句sql_text
    #ora_exp "select remark from md.proc_step_log where proc_name='${proc_name}' and end_time like '${log_time}%' and step_result=1" "${PATH_LOG}/proc_bad_sql.tmp"
    #复制日志文件到本地
    expect ${PATH_LOG}/expect_scp.sh 10.11.72.53 shdw 1zhxcqL$ /data1/pst-proc-1.0.0-SNAPSHOT/logs/${log_time}/${proc_name}.log ${PATH_LOG}/proclog/
    if [ $? -eq 0 ]; then
      #截取bad SQL grammar语句
      num=$(cat ${PATH_LOG}/proclog/${proc_name}.log | sed -n "/bad SQL grammar/=" | tail -1)
      sed -n "$num,/SQLSyntaxErrorException/p" ${PATH_LOG}/proclog/${proc_name}.log >${PATH_LOG}/proc_bad_sql.tmp
      rm -f ${PATH_LOG}/proclog/${proc_name}.log
      #sql解析表名
      sql_cnt=$(cat ${PATH_LOG}/proc_bad_sql.tmp | wc -l)
      if [ ${sql_cnt} -gt 0 ]; then
        ora_code=$(cat ${PATH_LOG}/proc_bad_sql.tmp | awk -F "SQLSyntaxErrorException" '{print $2}' | awk NF | awk -F ":" '{print $2}')
        cat ${PATH_LOG}/proc_bad_sql.tmp | tr '[a-z]' '[A-Z]' | tr "\t" " " | tr -s " " | tr " " "\n" | tr -s "\n" >${PATH_LOG}/proc_bad_sql_a.tmp
        insert_user=$(cat ${PATH_LOG}/proc_bad_sql_a.tmp | awk '/INTO/{getline;print}' | awk -F "." '{print $1}')
        #Write_Log_File "${insert_user}"
        cat ${PATH_LOG}/proc_bad_sql_a.tmp | awk '/JOIN/{getline;print}' >${PATH_LOG}/table_list.tmp
        cat ${PATH_LOG}/proc_bad_sql_a.tmp | awk '/FROM/{getline;print}' >>${PATH_LOG}/table_list.tmp
        table_list=$(cat ${PATH_LOG}/proc_bad_sql_a.tmp | awk '/FROM/{getline;print}')
        echo ${table_list} | while read table_name; do
          table_cnt=$(cat proc_bad_sql_a.tmp | awk '/'$table_name'/{getline;print}' | awk -F "," '{print NF}')
          if [ ${table_cnt} -gt 1 ]; then
            cat proc_bad_sql_a.tmp | tr "\n" " " | awk -F "$table_name" '{print $2}' | awk -F "WHERE" '{print $1}' | awk -F "," '{for(i=1;i<NF;i++)printf("%s",$i" ");print $NF}' >>${PATH_LOG}/table_list.tmp
          fi
        done
        #sql解析表名结束，开始检查缺表，缺权限
        cat ${PATH_LOG}/table_list.tmp | while read table_name; do
          if [ -n "${table_name}" ]; then
            table_length=$(echo ${table_name} | wc -c)
            table_str=$(echo $table_name | grep -c ^\()
            if [ ${table_length} -gt 2 -a ${table_str} -eq 0 ]; then
              if [ ${ora_code} = "ORA-00942" ]; then
                #连接33库检查该表的个数为1，-eq 0 >echo 缺表
                run_ora_sql "select count(*) from dba_tables where trim(owner)||'.'||trim(table_name)='${table_name}'"
                now_num=$(echo ${ReturnStr} | sed 's/ //g')
                #Write_Log_File "表${table_name},33库有${now_num}张"
                if [ ${now_num} -eq 0 ]; then
                  echo "${table_name}" >>${PATH_LOG}/error_msg.tmp
                fi
              elif [ ${ora_code} = "ORA-01031" ]; then
                table_user=$(echo ${table_name} | awk -F "." '{print $1} ')
                if [ "${table_user}" != "${insert_user}" ]; then
                  run_ora_sql "SELECT count(1) FROM DBA_TAB_PRIVS WHERE trim(owner)||'.'||trim(table_name)='${table_name}' and grantee='${insert_user}'"
                  now_num=$(echo ${ReturnStr} | sed 's/ //g')
                  if [ ${now_num} -eq 0 ]; then
                    echo "${insert_user};${table_name}" >>${PATH_LOG}/error_msg.tmp
                  fi
                fi
              else
                echo "${ora_code}" >>${PATH_LOG}/error_msg.tmp
              fi
            fi
          fi
        done #table_list.tmp循环结束
        if [ -f ${PATH_LOG}/error_msg.tmp ]; then
          error_cnt=$(cat ${PATH_LOG}/error_msg.tmp | wc -l)
          if [ ${error_cnt} -gt 1 ]; then
            SQLERRMC=$(cat ${PATH_LOG}/error_msg.tmp | tr '\n' ',')
          else
            SQLERRMC=$(cat ${PATH_LOG}/error_msg.tmp)
          fi
        else
          if [ ${ora_code} = "ORA-00942" ]; then
            SQLERRMC=",现在表已有"
          elif [ ${ora_code} = "ORA-01031" ]; then
            SQLERRMC=",现在权限已有"
          else
            SQLERRMC="未查到报错信息"
          fi
          Write_Log_File "error_msg.tmp文件不存在，没有解析到表名"
        fi
      else
        SQLERRMC="未找到bad SQL grammar语句"
        ora_code="未找到"
      fi
    else
      SQLERRMC="未找到日志"
      ora_code="未找到"
    fi
    SQLSTATE="未找到"
    echo "insert into db2info.proc_fail_log values('${groupname}','${proc_name}','${end_time}','${ora_code}','${SQLSTATE}','${SQLERRMC}','${mm}','${run_platform}' );" >>${PATH_LOG}/proc_fail_yt_sql.txt
    rm -f ${PATH_LOG}/error_msg.tmp

  done #yt_proc_fail.tmp的循环结束
  diff ${PATH_LOG}/yt_proc_fail.tmp ${PATH_LOG}/yt_proc_lastone_fail.tmp >/dev/null
  if [ $? -eq 0 ]; then
    Write_Log_File "检查yt挂起与上一次内容相同"
  else
    ${connmpp}
    db2 "delete from db2info.proc_fail_log where run_platform='DIM_RUN_PLATFORM_T001'"
    db2 -tvf ${PATH_LOG}/proc_fail_yt_sql.txt
    Write_Log_File "yt挂起信息更新"
    db2 connect reset
  fi

}
#应用库YT机
check_app() {

}

check_mp() {
  check_mpp
  check_yt
}

#===============================main===============================
sh_name=$(echo ${0} | awk -F"/" '{print $NF}' | awk -F"." '{print $1}')
machine_name=${1}
machine_name=mp
YYYYMMDD=$(date +%Y%m%d)
PATH_LOG="/code/crm/crmbm/work/qixx"
YYYYMMDD_2D=$(/code/crm/crmbm/work/extract/config/add_date -2)
rm -f ${PATH_LOG}/proc_fail_log_${YYYYMMDD_2D}.log
Log_File="${PATH_LOG}/proc_fail_log_${YYYYMMDD}.log"
check_mp
