package DatePractice;
import java.util.Date;

public class Practice01 {
    public static void main(String[] args){
//        Date:构造方法：Date(); Date(long date) 根据指定的毫秒值创建对象自 1970年的7月1日000起；
        Date date = new Date();//常常不书写，无实际意义。
        System.out.println(date);
        Date date2 = new Date(1000*60*60);
        System.out.println(date2);
//        成员方法 setTime(); getTime(long time)
        System.out.println("===成员方法===");
        System.out.println(date.getTime());//自1970年7月1日起：当前时间的毫秒值
        date.setTime(1000*60*60);
        System.out.println(date.getTime());
    }
}
