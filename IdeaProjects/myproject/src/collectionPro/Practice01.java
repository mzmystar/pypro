package collectionPro;
import java.util.Collection;
import java.util.ArrayList;

public class Practice01 {
    /*
    * boolean add(E e) 添加元素 E 指代各种基本数据类型
    * boolean remove(Object o) 移除元素
    * void clear() 清空集合内元素
    * boolean contains(Object o) 判断集合内是否有该元素
    * boolean isEmpty() 判断集合是否为空
    * int size() 计算集合的长度，集合内元素的个数
    * */
    public static void main(String[] args){
        Collection<String> c = new ArrayList<>();
        c.add("hello");
        c.add("world");
        System.out.println("初始集合内元素："+c);
        System.out.println("检测集合是否为空："+c.isEmpty());
        System.out.println("计算集合内的元素个数："+c.size());
        System.out.println("检测集合内是否存在该hello元素："+c.contains("hello"));
        System.out.println("移除集合内的hello元素："+c.remove("hello"));
        System.out.println("移除集合内某元素后："+c);
        c.clear(); //清空集合内元素
        System.out.println(c.isEmpty());

    }
}
