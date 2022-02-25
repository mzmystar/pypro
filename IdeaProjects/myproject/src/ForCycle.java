import java.util.Scanner;

public class ForCycle {
//    求取俩个整数的和
    public static int qiuhe(int a,int b){
        return a+b;
    }
//    比较两个数值之间的大小关系
    public static int comp(int a,int b){
        if (a>b){
            return a;
        }else{
            return b;
        }
    }
//    求取百位数的水仙花数
    public static void wFlowers(){
        for(int i=100;i<1000;i++){
            int ge = i%10;
            int shi = i/10%10;
            int bai = i/100;
            if (ge*ge*ge+shi*shi*shi+bai*bai*bai==i){
                System.out.println(i+"是水仙花数");
            }
        }
    }
    public static void main(String[] args){
//    单层for循环
//        for (int i=1;i<=10;i++){
//            System.out.println(i);
//        }
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入两个数：");
        int a =sc.nextInt();
        int b =sc.nextInt();
        int res = qiuhe(a,b);
        System.out.println("两数和为："+res);
        int larger = comp(a,b);
        System.out.println("两者之间数值较大者是:"+larger);
        wFlowers();
    }


}
