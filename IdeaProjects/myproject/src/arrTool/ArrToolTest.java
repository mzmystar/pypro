package arrTool;

import java.util.Arrays;

public class ArrToolTest {
    public static void main(String[] args){
        int arr[] = {1,5,9,2,1,4,7};
        System.out.print("排序前："+Arrays.toString(arr));
        Arrays.sort(arr);
        System.out.print("排序后："+Arrays.toString(arr));
    }
}
