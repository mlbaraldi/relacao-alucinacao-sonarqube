package generated;
public class Generated8b0123611be9 {
public void putAllWriteable(BeanMap map){
    if(map == null) {
        throw new IllegalArgumentException("map cannot be null");
    }

    for(Map.Entry<String, Object> entry : map.entrySet()){
        if(entry.getValue() != null){
            this.put(entry.getKey(), entry.getValue());
        }
    }
}
}
