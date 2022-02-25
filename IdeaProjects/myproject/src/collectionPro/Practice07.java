package collectionPro;

import java.util.ArrayList;
import java.util.List;

public class Practice07 {
    public static void main(String[] args) {
        /*
         * 增强for
         * for(元素的数据类型 变量名 : 数组名或Collection集合对象名)
         * 简化了数组的遍历；弊端：必须先进行非NULL判断
         *
         * */
        List<String> list = new ArrayList<>();
        list.add("hello");
        list.add("world");
//        增强for 循环
        if (list != null) {
            for (String s : list) {
                System.out.println(s);
            }
        }
    }
}
