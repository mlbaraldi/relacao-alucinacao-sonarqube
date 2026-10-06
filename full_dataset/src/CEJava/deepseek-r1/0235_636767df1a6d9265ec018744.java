package generated;
public class Generated7c9748f01d95 {
protected List<TimeRange> buildTimeRanges(long start,long end){
    List<TimeRange> ranges = new ArrayList<>();
    long currentStart = start;
    while (currentStart < end) {
        long currentEnd = currentStart + FETCH_DATA_DURATION;
        if (currentEnd > end) {
            currentEnd = end;
        }
        ranges.add(new TimeRange(currentStart, currentEnd));
        currentStart = currentEnd;
    }
    return ranges;
}
}
