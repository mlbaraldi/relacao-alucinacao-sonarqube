package generated;
public class Generated00ae330a6121 {
public void put(LoggingEvent o){
    synchronized (queue) {
        while (queue.size() == capacity) {
            queue.wait();
        }
        queue.add(event);
        queue.notifyAll();
    }
}
}
