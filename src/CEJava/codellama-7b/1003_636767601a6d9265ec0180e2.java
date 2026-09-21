package generated;
public class Generatedb8cde3932da4 {
private List<Pair<List<Pair<Integer,Integer>>,E>> computeGlobalSeparatorList(){
    List<Pair<List<Pair<Integer, Integer>>, E>> separatorList = new ArrayList<>();

    for (E edge : graph.getEdges()) {
        List<Pair<Integer, Integer>> minimalSeparators = new ArrayList<>();

        for (E neighbor : graph.getNeighbors(edge)) {
            List<Pair<Integer, Integer>> separators = computeMinimalSeparators(neighbor);
            minimalSeparators.addAll(separators);
        }

        separatorList.add(new Pair<>(minimalSeparators, edge));
    }

    return separatorList;
}
}
