package collectionPro;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Iterator;

public class Practice02 {
    public static void main(String[] args){
        /*迭代器 ：集合遍历的一种方式，依赖于集合而存在，类似于c的指针
         *集合遍历：Iterator() 迭代器
         * 方法：E next()
         * boolean hasNext()
         */
        Collection<String> c = new ArrayList<>();
        c.add("hello");
        c.add("world");
        c.add("java");
        Iterator it = c.iterator();
        while(it.hasNext()){
            System.out.println(it.next());
        }


    }
}
