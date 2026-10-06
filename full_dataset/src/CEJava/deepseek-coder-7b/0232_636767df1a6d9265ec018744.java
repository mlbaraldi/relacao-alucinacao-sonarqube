package generated;
public class Generated7c9748f01d95 {
protected List<TimeRange> buildTimeRanges(long start,long end){
    List<TimeRange> timeRanges = new ArrayList<>();

    while (start < end) {
        long newEnd = Math.min(start + FETCH_DATA_DURATION, end);
        timeRanges.add(new TimeRange(start, newEnd));
        start = newEnd;
    }

    return timeRanges;
}
}
