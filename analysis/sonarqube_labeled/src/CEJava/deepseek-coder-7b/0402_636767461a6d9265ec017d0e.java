package generated;
public class Generatede69b21513209 {
private Pair<List<Integer>,Long> computeSuffixSum(List<Integer> bounds){
    List<Integer> suffixSums = new ArrayList<>();
    long sum = 0;

    for (int i = bounds.size() - 1; i >= 0; i--) {
        sum += bounds.get(i);
        suffixSums.add(0, (int) sum);
    }

    return new Pair<>(suffixSums, sum);
}
}
