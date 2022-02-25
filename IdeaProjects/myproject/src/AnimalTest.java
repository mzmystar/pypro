public class AnimalTest {
//    主函数
    public static void main(String[] args){
//      实例化对象
        Animals animals=new Animals();//很少这样使用，无实际意义。
        animals.voice = "汪汪";
        animals.age = 1;
        animals.shout();
        System.out.println("------------子类调用---------------");
        Cat cat = new Cat();
//      方法重载
        cat.shout();
//      子类调用父类的成员方法
        cat.setAge(2);
        int res=cat.getAge();
        System.out.println("喵喵的年龄："+res);
//      多态
        System.out.println("--------多态的实例----------------");

        Animals a = new Cat();
        a.setVoice("汪汪汪");
        a.shout(); //调用了子类的shout()方法
//        a.hobby(); 无法调用子类特有方法
//        多态的转型
        Cat cat1 = (Cat) a;
        cat1.hobby();
    }
}
