package mixTest;


import java.util.Scanner;

public class BlString {
    public static void main(String[] args){
//        遍历字符串
        Scanner sc = new Scanner(System.in);
        System.out.println("输入一个字符串:");
        String str = sc.nextLine();
        int n = str.length();//获取字符串的长度
        for(int i=0;i<n;i++){
            System.out.print(str.charAt(i)+" ");
        }
    }
}
