package generated;
public class Generated00ae330a6121 {
public void put(LoggingEvent o){
    if (index < BUFFER_SIZE) {
        buffer[index] = o;
        index++;
    }
    // if the buffer is full, the event is silently dropped
}
}
