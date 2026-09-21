package generated;
public class Generatedf3583c188ee2 {
public boolean isExpired(long timestamp,long expiredThreshold){
    long currentTime = System.currentTimeMillis();
    long timeDifference = currentTime - timestamp;

    if (timeDifference > expiredThreshold) {
        return true;
    } else {
        return false;
    }
}
}
