import java.util.LinkedList;

public class Storage {
    private final int MAX_SIZE = 100;
    private LinkedList<Object> list = new LinkedList<>();

    public void produce(String producer) {
        synchronized (list) {
            while (list.size() == MAX_SIZE) {
                System.out.println("仓库已满，[" + producer + "]暂时不能生产！");
                try {
                    list.wait();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            list.add(new Object());
            System.out.println(producer + "生产了一个产品，现储量为" + list.size());
            list.notifyAll();
        }
    }

    public void consume (String consumer) {
        synchronized (list) {
            while (list.size() == 0) {
                System.out.println("仓库已空，[" +consumer + "]暂时不能消费！");
                try {
                    list.wait();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            list.remove();
            System.out.println(consumer + "消费了一个产品，现储量为" + list.size());
            list.notifyAll();
        }
    }

    public static void main(String[] args) {
        Storage storage = new Storage();
        for (int i = 1; i < 5; i++) {
            int finalI = i;
            new Thread(new Runnable(){
                @Override
                public void run() {
                    storage.produce(String.format("生产者%d:", finalI));
                }
            }).start();
        }
        for (int i = 1; i < 5; i++) {
            int finalI = i;
            new Thread(new Runnable(){
            
                @Override
                public void run() {
                    storage.consume(String.format("消费者%d:", finalI));
                }
            }).start();
        }
    }
}