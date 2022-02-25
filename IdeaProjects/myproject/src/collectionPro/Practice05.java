package collectionPro;

import java.util.ArrayList;
import java.util.List;
import java.util.ListIterator;
import java.util.Iterator;

public class Practice05 {
    public static void main(String[] args){
        /*
        * ListIterator 列表迭代器
        * ListIterator<E> listIterator() 返回此列表元素的列表迭代器
        * 特有功能：可以逆向遍历，但要求必须先正向遍历 ：//自己理解：以C解释，用以将指针指向末端。
        * E previous()
        * boolean hasPrevious()
        * */
        List<String> list = new ArrayList<>();
        list.add(0,"o号位");
        list.add(1,"1号位");
        list.add(2,"2号位");
        list.add(3,"3号位");

        ListIterator<String> li = list.listIterator();
        while(li.hasNext()){
            String s1 = li.next();
            System.out.println(s1);
        }
        System.out.println("逆向遍历：");
        while(li.hasPrevious()){
            String s1 = li.previous();
            System.out.println(s1);
        }
    }
}
