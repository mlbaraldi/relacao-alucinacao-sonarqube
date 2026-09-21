package generated;
public class Generatedca102d061f10 {
public void removeAppender(String name){
    Iterator<Appender> iterator = appenders.iterator();
    while (iterator.hasNext()) {
        Appender appender = iterator.next();
        if (Objects.equals(name, appender.getName())) {
            iterator.remove();
            break;
        }
    }
}
}
