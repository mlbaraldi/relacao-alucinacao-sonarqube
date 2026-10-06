package generated;
public class Generated8433671cb64b {
public Logger exists(String name){
    if (this.loggerMap.containsKey(name)) {
        return this.loggerMap.get(name);
    } else {
        return null;
    }
}
}
