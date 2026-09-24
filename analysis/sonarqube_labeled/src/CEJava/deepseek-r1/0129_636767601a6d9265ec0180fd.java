package generated;
public class Generated11a045ec5994 {
protected void addToIndex(V sourceVertex,V targetVertex,E e){
    // Assuming 'index' is a class member variable of type Map<V, Map<V, List<E>>>
    index.computeIfAbsent(sourceVertex, k -> new HashMap<>())
         .computeIfAbsent(targetVertex, k -> new ArrayList<>())
         .add(e);
}
}
