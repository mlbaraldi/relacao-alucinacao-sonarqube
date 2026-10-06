package generated;
public class Generatede69b21513209 {
private Pair<List<Integer>,Long> computeSuffixSum(List<Integer> bounds){
    if (bounds.isEmpty()) {
        return new Pair<>(Collections.emptyList(), 0L);
    }

    long totalSum = 0L;
    List<Integer> suffixSums = new ArrayList<>();

    for (int i = bounds.size() - 1; i >= 0; i--) {
        totalSum += bounds.get(i);
        suffixSums.add((int) totalSum);
    }

    Collections.reverse(suffixSums);

    return new Pair<>(suffixSums, totalSum);
}
}
