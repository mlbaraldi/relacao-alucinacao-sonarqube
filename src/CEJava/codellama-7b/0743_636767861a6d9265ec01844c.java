package generated;
public class Generatedca102d061f10 {
public void removeAppender(String name){
    for (int i = 0; i < appenders.size(); i++) {
        if (appenders.get(i).getName().equals(name)) {
            appenders.remove(i);
            break;
        }
    }
}
}
