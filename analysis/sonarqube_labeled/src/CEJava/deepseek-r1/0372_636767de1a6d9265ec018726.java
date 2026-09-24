package generated;
public class Generated36c86b8373d0 {
public List<SequenceRange> buildSequenceRanges(){
    List<SequenceRange> ranges = new ArrayList<>();
    // Retrieve the current profile's segments snapshot
    List<Segment> segments = getCurrentProfileSnapshotSegments();
    for (Segment segment : segments) {
        ranges.add(new SequenceRange(segment.getStart(), segment.getEnd()));
    }
    return ranges;
}
}
