package person;

public class Teacher extends Person {
    @Override
    public void eat(){
        System.out.println("教师吃饭");
    }
    @Override
    public void sleep(){
        System.out.println("教师也要睡觉");
    }
    public void teach(){
        System.out.println("教师要备课教学");
    }
}
