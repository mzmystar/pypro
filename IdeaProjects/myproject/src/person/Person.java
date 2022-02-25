package person;

public abstract class Person {
    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    /*
        抽象类：可有抽象方法
        抽象方法：一定有抽象类
        抽象类不能实例化
        抽象类成员变量：
            变量或者常量
        抽象类的子类：
            要么是抽象类
            要么重写抽象类的所有抽象方法
         */

    private int age;
    private String name;
    public abstract void eat();
    public abstract void sleep();
}
