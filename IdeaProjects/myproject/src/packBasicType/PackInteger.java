package packBasicType;

public class PackInteger {
    public static void main(String[] args){
        int value = 100;
        Integer i = new Integer(value);
        System.out.println(i);
        System.out.println("***********************************************");
//        数字字符串转数字int类型
        String s = "1001";
        Integer si = new Integer(s);
        System.out.println(si);

    }
}
