package generated;
public class Generated8d36eb61437c {
public boolean isAttached(Appender appender){
    if (appender == null) {
        return false;
    }
    for (Appender a : appenders) {
        if (a == appender) {
            return true;
        }
    }
    return false;
}
}
