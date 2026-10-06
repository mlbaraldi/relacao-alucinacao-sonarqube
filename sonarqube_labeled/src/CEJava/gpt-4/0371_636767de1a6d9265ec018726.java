package generated;
public class Generated36c86b8373d0 {
public List<SequenceRange> buildSequenceRanges(){
    List<SequenceRange> sequenceRanges = new ArrayList<>();

    // Assuming we are building sequence ranges from 1 to 10 for this example
    for (int i = 1; i <= 10; i++) {
        sequenceRanges.add(new SequenceRange(i, i+1));
    }

    return sequenceRanges;
}
}
