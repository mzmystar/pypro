package paixu;


public class MaoPao {
    public static void compArray(int[] arr){
        for(int i=0;i<arr.length-1;i++){
            for(int j=0;j<arr.length-1-i;j++){
                if(arr[j]>arr[j+1]){
                    int temp=arr[j+1];
                    arr[j+1]=arr[j];
                    arr[j]=temp;
                }
            }
        }
    }
    public static void main(String[] args){
//        定义一个数组
        int[] arr = {23,24,27,28,5,17};
        compArray(arr);
        for(int i=0;i<arr.length;i++){
            System.out.println(arr[i]);
        }
    }

}
