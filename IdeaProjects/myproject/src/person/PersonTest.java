package person;

public class PersonTest {
    public static void main(String[] args){
//      使用多态  实例化一个人 ：学生
        Person s = new Student();
        s.sleep();
        s.eat();
//       使用多态 实例化一个人：教师
        Person t = new Teacher();
        t.eat();
        t.sleep();
//       使用多态 实例化一个人：英文教师
        Person et = new EnglishTeacher();
        et.sleep();

        EnglishTeacher et1=(EnglishTeacher) et;
//        调用独有方法
        et1.major();
        et1.speakEnglish();
    }
}
