package DatePractice;
import java.util.Date;
import java.text.SimpleDateFormat;
import java.text.ParseException;

/*工具类：构造方法私有，   成员方法静态
* */

public class Practice03 {
    private  Practice03(){}
    public String  dateToString(Date d,String format){
        SimpleDateFormat sdf = new SimpleDateFormat(format);
        String s = sdf.format(d);
        return s;
    }
    public Date stringToDate(String s ,String format) throws ParseException{
        SimpleDateFormat sdf = new SimpleDateFormat(format);
        Date date = new Date();
        date = sdf.parse(s);
        return date;
    }
    public static void main(String[] args) throws ParseException{
        Date d = new Date();
        Practice03 p3 = new Practice03();
        String str = p3.dateToString(d,"yyyy-MM-dd HH:mm:ss");
        System.out.println("格式化时间："+str);
        Date dd = p3.stringToDate("2021-12-21","yyyy-MM-dd");
        System.out.println("时间解析："+dd);
    }
}
