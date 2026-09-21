package generated;
public class Generated04fb7c992a92 {
int addType(final String value){
    if (!typeMap.containsKey(value)) {
        typeMap.put(value, nextIndex++);
    }
    return typeMap.get(value);
}
}
