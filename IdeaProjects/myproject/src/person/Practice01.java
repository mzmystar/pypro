package person;

import java.util.*;

/*
*   (1)生成10个1至100之间的随机整数(不能重复)，存入一个List集合
    (2)然后利用迭代器和增强for循环分别遍历集合元素并输出
* */
public class Practice01 {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        Random rand  = new Random();
        System.out.println(rand.nextInt(101));
        List<Integer> list = new ArrayList<>();

        for(int count=0;count<10;count++){
            int temp = rand.nextInt(101);
            if (list.contains(temp)){
                count--;
            }else{
                list.add(temp);
            }
        }
        for(Integer num:list){
            System.out.print(num+" ");
        }
        Iterator<Integer> it = list.iterator();
        System.out.println("迭代器：");
        while(it.hasNext()){
            System.out.print(it.next()+" ");
        }
    }
}
