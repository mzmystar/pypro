package classTest;

public class Animals {
//    成员变量
    protected int age;
    protected String color;
    protected String voice;
//    普通方法
    public void shout(){
        System.out.println(this.voice);
    }
//    成员方法
    public int getAge() {
        return age;
    }
    public void setAge(int age) {
        this.age = age;
    }

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public String getVoice() {
        return voice;
    }
    public void setVoice(String voice){
        this.voice=voice;
    }
//    构造方法 无参数
    public  Animals(){
        System.out.println("无参数构造方法");
    }

//    直接输出对象名
    @Override
    public String toString() {
        return "classTest.Animals{" +
                "age=" + age +
                ", color='" + color + '\'' +
                ", voice='" + voice + '\'' +
                '}';
    }

}
