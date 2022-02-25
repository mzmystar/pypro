package stringbuilder;

import java.util.Scanner;

public class StringBuilderTest3 {
//    字符串反转
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.println("请输入字符串：");
        String s = scan.nextLine();
        StringBuilder sb = new StringBuilder(s);
        String sf = sb.reverse().toString();
        System.out.println("反转："+sf);
    }
}
