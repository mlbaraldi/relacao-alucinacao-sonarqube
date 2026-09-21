package generated;
public class Generated8b0123611be9 {
public void putAllWriteable(BeanMap map){
    for (Object key : map.keySet()) {
        if (this.isWriteable(key)) {
            this.put(key, map.get(key));
        }
    }
}
}
