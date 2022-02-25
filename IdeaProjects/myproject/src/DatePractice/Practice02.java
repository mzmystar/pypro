package DatePractice;
import java.text.ParseException;
import java.util.Date;
import java.text.SimpleDateFormat;

public class Practice02 {
    public static void main(String[] args) throws ParseException {
//        SimpleDateFormat :是一个以与语言环境有关的方式来格式化和解析日期的具体类
//      解析：public static Date  parse(String s)  文本 --> 日期 ；
//      格式化：public final String format(Date date) 日期--> 文本
        Date d = new Date();
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy年MM月dd日 HH-mm-ss");
        String str = sdf.format(d);
        System.out.println(str);
//        解析：
        String s = "2021-11-08 14:50:00";
        SimpleDateFormat sdf1 = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
        Date date = sdf1.parse(s);//要添加一个解析异常抛出 ParseException
        System.out.println(date);
    }

}
