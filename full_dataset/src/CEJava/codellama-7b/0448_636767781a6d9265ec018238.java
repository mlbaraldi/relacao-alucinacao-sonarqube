package generated;
public class Generated8d36eb61437c {
public boolean isAttached(Appender appender){
    for (Appender attachedAppender : attachedAppenders) {
        if (attachedAppender.equals(appender)) {
            return true;
        }
    }
    return false;
}
}
