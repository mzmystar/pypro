package packBasicType;

import java.util.Arrays;

public class Practice01 {
    public static void main(String[] args){
//        将字符串 “ 14 23 45 42 31 7 ” 转化为 “ 7 14 23 31 42 45 ”
//        思路：分割；数组；排序；拼接
        String  s = "14 23 45 42 31 7";
        String[] strArray = s.split(" ");
//        for(int i =0 ;i<strArray.length;i++){
//            System.out.println(strArray[i]);
//        }
        int[] arr = new int[strArray.length];
        for(int i=0;i<arr.length;i++){
            arr[i]=Integer.parseInt(strArray[i]);
        }
        Arrays.sort(arr);
        StringBuilder sb = new StringBuilder();
        for(int i=0;i<arr.length;i++){
            if(i==arr.length-1){
                sb.append(arr[i]);
            }else{
                sb.append(arr[i]).append(" ");
            }
        }
        String ns = sb.toString();
        System.out.println("结果："+ns);

    }
}
