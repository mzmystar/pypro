package stringbuilder;

public class StringBuilderTest2 {
    public static String arrToString(int arr[]){
        StringBuilder sb = new StringBuilder();
        sb.append("[");
        for(int i=0;i<arr.length;i++){
            if(i==arr.length-1){
                sb.append(arr[i]);
            }else{
                sb.append(arr[i]).append(",");
            }
        }
        sb.append("]");
        String s = sb.toString();
        return s;
    }
    public static void main(String[] args){
//        例子：将数组{1,2,3} 转化为 [1,2,3]
        int arr[]={1,2,3,4};
        String s = arrToString(arr);
        System.out.println(s);
    }
}
