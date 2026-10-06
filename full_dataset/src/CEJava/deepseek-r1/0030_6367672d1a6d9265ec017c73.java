package generated;
public class Generated6f87ec9c5513 {
public boolean shouldPrintMessage(int timestamp,String message){
    if (messageMap.containsKey(message)) {
        int lastTime = messageMap.get(message);
        if (timestamp - lastTime >= 10) {
            messageMap.put(message, timestamp);
            return true;
        } else {
            return false;
        }
    } else {
        messageMap.put(message, timestamp);
        return true;
    }
}
}
