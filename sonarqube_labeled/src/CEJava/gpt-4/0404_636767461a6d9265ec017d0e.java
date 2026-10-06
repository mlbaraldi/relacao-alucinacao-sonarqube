package generated;
public class Generatede69b21513209 {
private Pair<List<Integer>,Long> computeSuffixSum(List<Integer> bounds){
    List<Integer> suffixSum = new ArrayList<>();
    long totalSum = 0;
    int sum = 0;
    for (int i = bounds.size() - 1; i >= 0; i--) {
        sum += bounds.get(i);
        suffixSum.add(sum);
        totalSum += bounds.get(i);
    }
    Collections.reverse(suffixSum);
    return new Pair<>(suffixSum, totalSum);
}
}
