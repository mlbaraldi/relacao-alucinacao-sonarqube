package generated;
public class Generated04fb7c992a92 {
int addType(final String value){
    if (!this.typeTable.containsKey(value)) {
        this.typeTable.put(value, this.nextIndex);
        this.nextIndex++;
    }
    return this.typeTable.get(value);
}
}
