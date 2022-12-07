package person;

public class ThreadPractice implements Runnable{
    private static int tickets=100;
    public void run(){
        while (true){
            synchronized (this){
                if (tickets>0){
                    try{
                        Thread.sleep(1);
                    }catch (Exception e){

                    }
                    System.out.println(Thread.currentThread().getName() + "出票："+tickets);
                    tickets --;
                }
            }
        }
    }
}
