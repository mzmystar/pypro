package collectionPro;

import java.util.ArrayList;
import java.util.List;
import java.util.LinkedList;
import java.util.Iterator;

public class Practice08 {
    public static void main(String[] args){
        /*
        * 栈：先进后出
        * 队列：先进先出
        * 数组：查询快，增删慢
        * 链表：查询慢，增删快
        *      链表每个元素的末端有一个指向下一个数据的地址
        * List:子类
        *   ArrayList: 底层数据结构为数组
        *   LinkedList:底层数据结构为链表
        * */
        List<String> ll = new LinkedList<>();
        List<String> al = new ArrayList<>();
        ll.add("java");ll.add("c");ll.add("python");
        al = ll;al.add("PHP");
//        增强for
        System.out.println("链表:");
        for(String s:ll){
            System.out.print(s+" ");
        }
//        普通for
        System.out.println("数组：");
        for(int i=0;i<al.size();i++){
            String s = al.get(i);
            System.out.print(s+" ");
        }
//        迭代器
        Iterator<String> it = ll.iterator();
        while(it.hasNext()){
            String s = it.next();
            System.out.println(s);
        }

    }
}
