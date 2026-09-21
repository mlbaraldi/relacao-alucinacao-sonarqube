package generated;
public class Generated6f87ec9c5513 {
public boolean shouldPrintMessage(int timestamp,String message){
    int currentTimestamp = (int) (System.currentTimeMillis() / 1000);
    int difference = currentTimestamp - timestamp;
    if (difference > 10) {
        System.out.println(message);
        return true;
    } else {
        return false;
    }
}
}
