import java.util.Scanner;

public class Myself{
    public static void main(String[] args){
        int a = 10;
        int b = 20;
        float res;
        res = sum(a,b);
        int max_num = comp();
        System.out.println(res);
        System.out.println(max_num);
    }
    //两数和
    public static float sum(float a,float b){
        return a+b;
    }

    public static int comp(){
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入第一个数");
        int a = sc.nextInt();
        System.out.println("请输入第二个数");
        int b = sc.nextInt();
        if(a>b){
            return a;
        }else{
            return b;
        }
    }
}