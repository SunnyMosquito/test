// 继承Thread类实现线程，需要重写run方法
// public class ThreadTest extends Thread {
//     private int count = 10;
//     public void run() {
//         while (true) {
//             System.out.println(count + " ");
//             if (--count == 0) {
//                 return;
//             }
//         }
//     }

//     public static void main(String[] args) {
//         ThreadTest thread = new ThreadTest();
//         thread.start();
//     }
// }


// 实现Runnable接口
public class ThreadTest {
    public static void main(String[] args) {
        Thread thread = new Thread(new ThreadRunnable());
        thread.start();
    }
}

class ThreadRunnable implements Runnable {
    private int count = 10;

    public void run() {
        while (true) {
            System.out.println(count);
            if (--count == 0) {
                return;
            }
        }
    }
}