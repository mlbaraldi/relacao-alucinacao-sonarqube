package generated;
public class Generated04fb7c992a92 {
int addType(final String value){
    for (int i = 0; i < typeTable.size(); i++) {
        if (typeTable.get(i).value.equals(value)) {
            return i;
        }
    }
    Symbol typeSymbol = new Symbol(Symbol.TYPE, value);
    typeTable.add(typeSymbol);
    return typeTable.size() - 1;
}
}
