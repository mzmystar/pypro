public class p1 {
    public static void main(String[] args) throws ClassNotFoundException {
        // 方式1：类名.class
        Class clazz = String.class;
        // 输出clazz全名 就是包名.类名 java.lang.String
        System.out.println(clazz.getName());
        // 输出clazz精简名字 就是类名 String
        System.out.println(clazz.getSimpleName());
    }
    }