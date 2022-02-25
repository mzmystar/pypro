package packBasicType;

public class TranIntString {
    public static void main(String[] args){
//        类型转换 int string
//        int --> String
        int i = 100;
        String s = String.valueOf(i);
        System.out.println(s);
        System.out.println("_______________________________________");
//        string --> int
        String s1 = "1001";
        int i1 = Integer.parseInt(s1);
        System.out.println("转化后结果："+i1);

    }
}
