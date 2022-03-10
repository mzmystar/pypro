package classTest;

public class Cat extends Animals{
//  重载父类方法
    public void shout(){
        System.out.println("喵喵叫");
    }
//  子类特有方法
    public void hobby(){
        System.out.println("玩毛球");
    }
//  子类构造方法
    public Cat(){
//        默认带有一个：super();指向父类的构造方法。
        System.out.println("子类无参数构造方法");
    }
}
