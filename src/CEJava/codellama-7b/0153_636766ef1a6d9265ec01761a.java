package generated;
public class Generated04fb7c992a92 {
int addType(final String value){
    // Check if the type table already contains a similar type
    for (int i = 0; i < types.size(); i++) {
        if (types.get(i).getValue().equals(value)) {
            return i;
        }
    }

    // If the type table does not contain a similar type, create a new type Symbol
    TypeSymbol typeSymbol = new TypeSymbol(value);
    types.add(typeSymbol);
    return types.size() - 1;
}
}
