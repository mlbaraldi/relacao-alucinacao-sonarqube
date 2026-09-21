package generated;
public class Generated11a045ec5994 {
protected void addToIndex(V sourceVertex,V targetVertex,E e){
    if (!adjList.containsKey(sourceVertex)) {
        adjList.put(sourceVertex, new ArrayList<>());
    }
    adjList.get(sourceVertex).add(new Edge<>(targetVertex, e));
}
}
