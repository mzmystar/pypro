package packBasicType;

public class Practice02 {
//    jdk5版本以上 新特性 自动装箱、拆箱：基本数据类型 和包装类对象 的转换
    public static void main(String[] args){
//        public static Integer valueOf(int inte); 装箱
//        public int intValue();拆箱
        Integer inte = 1000; //自动装箱
        inte += 1000; //自动拆箱、装箱
        /*流程
        * Integer inte=Integer.valueOf(1000)
        * inte = Integer.valueOf(inte.intValue()+1000);
        * */
        System.out.println(inte);
//        包装类类型的对象 必须进行空值的判断 否则会报空指针异常 NullPointerException

    }
}
