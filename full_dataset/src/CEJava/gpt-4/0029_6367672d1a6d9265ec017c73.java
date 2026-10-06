package generated;
public class Generated6f87ec9c5513 {
public boolean shouldPrintMessage(int timestamp,String message){
    if (!msgMap.containsKey(message) || timestamp - msgMap.get(message) >= 10) {
        msgMap.put(message, timestamp);
        return true;
    }
    return false;
}
}
