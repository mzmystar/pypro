package person;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class ThreadTest {
    public static void main(String[] args) {
//        创建任务类对象
        ThreadPractice tp = new ThreadPractice();
//       创建线程池对象 从线程池中获取两个线程
        ExecutorService es = Executors.newFixedThreadPool(2);
//        创建线程对象
//        自定义线程对象，调用
//        Thread t = new Thread(tp);
//        t.start();
//        从线程池中获取线程对象，调用对象tp 内的run()
        es.execute(tp);
        es.execute(tp);

    }
}
