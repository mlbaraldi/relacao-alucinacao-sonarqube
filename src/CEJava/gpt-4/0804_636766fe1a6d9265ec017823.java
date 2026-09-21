package generated;
public class Generated9f37ef8ceeb6 {
int addConstantNameAndType(final String name,final String descriptor){
    Symbol newSymbol = new Symbol(name, descriptor);

    if (!constantPool.containsKey(newSymbol)) {
        int newId = constantPool.size() + 1;
        constantPool.put(newSymbol, newId);
        return newId;
    } else {
        return constantPool.get(newSymbol);
    }
}
}
