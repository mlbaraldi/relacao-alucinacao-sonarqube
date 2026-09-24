package generated;
public class Generatede69b21513209 {
private Pair<List<Integer>,Long> computeSuffixSum(List<Integer> bounds){
    List<Integer> suffixSum = new ArrayList<>();
    Long totalSum = 0L;

    for (int i = bounds.size() - 1; i >= 0; i--) {
        totalSum += bounds.get(i);
        suffixSum.add(totalSum);
    }

    // Reverse the suffix sum list to get the correct order
    suffixSum = reverseList(suffixSum);

    return new Pair<>(suffixSum, totalSum);
}
}
