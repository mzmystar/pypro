package person;

public class Student extends Person {

    @Override
    public void eat() {
        System.out.println("学生吃食堂");
    }
    @Override
    public void sleep(){
        System.out.println("学生睡寝室");
    }
    public void study(){
        System.out.println("每天要上课");
    }
}
