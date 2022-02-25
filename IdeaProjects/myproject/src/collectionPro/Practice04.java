package collectionPro;

import java.util.ArrayList;
import java.util.List;
import java.util.Iterator;

public class Practice04 {
    public static void main(String[] args){
        //List<E>  E 指代各基本数据类型
        //集合序列List特性:有序、数据可重复
        List<String> list = new ArrayList<>();
        list.add("hello");list.add("world");list.add("hello");list.add("world");
        /*
         * List特有成员方法：
         * void add(int index,E e) 指定位置添加元素；
         * E remove(int index) 删除指定位置的元素，返回元素本身；,删除后序列位置会发生变化，在处理遍历时，易出错。
         * E get(int index) 获取指定位置的元素；
         * E set(int index,E e) 修改指定位置的元素；
         * */
        list.set(1,"java");
        System.out.println("修改后："+list.get(1));
        list.add(3,"666");
        list.remove(3); //删除后返回该位置的元素
        list.add(4,"666");//添加元素时注意List 长度，避免出现索引溢出问题

//        迭代器遍历List集合
        Iterator<String> it = list.iterator();
        while(it.hasNext()){
            System.out.print(it.next());
        }
//        for循环遍历 List集合
        for(int i=0;i<list.size();i++){
            String s = list.get(i);
            System.out.print(s);
        }
    }
}
