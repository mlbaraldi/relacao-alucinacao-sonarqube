package generated;
public class Generated04fb7c992a92 {
int addType(final String value){
    if (!typeTable.contains(value)) {
        typeTable.add(value);
    }
    return typeTable.indexOf(value);
}
}
