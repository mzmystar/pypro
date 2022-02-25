package stringbuilder;

public class StringBuilderTest {
    public  static void main(String[] args){
        String s1 = "string";
//        String 转 StringBuilder
        StringBuilder sb = new StringBuilder(s1);
        System.out.println(sb);
//        StringBuilder 转 String
        String s2 = sb.toString();
        System.out.println(s2);

    }
}
