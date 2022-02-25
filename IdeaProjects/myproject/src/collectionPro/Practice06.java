package collectionPro;

import java.util.ArrayList;
import java.util.ListIterator;
import java.util.List;

public class Practice06 {
    public static void main(String[] args){
        /*
        * 并发修改异常 ：在对集合用迭代器进行遍历的时候，如果通过对象对集合进行元素的修改，会发生该错误。
        * 处理：迭代器遍历时，通过迭代器进行修改；集合对象遍历时，用集合对象进行修改操作
        * */
        List<String> list = new ArrayList<>();
        list.add("hello");list.add("world");
        if(list.contains("hello")){
            list.add(0,"java");
        }
        System.out.println(list);
//        迭代器遍历
        ListIterator<String> it = list.listIterator();
        while(it.hasNext()){
            String s = it.next();
            if(s.equals("java")){
                it.add("python");
            }
            System.out.println(s);
        }
//        集合对象遍历
//        for(int i=0;i<list.size();i++){
//            if(list.contains("python")){
//                list.add("C语言");
//            }
//        }
        System.out.println(list);
    }
}
