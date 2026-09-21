package generated;
public class Generated7c9748f01d95 {
protected List<TimeRange> buildTimeRanges(long start,long end){
    List<TimeRange> timeRanges = new ArrayList<>();
    long duration = end - start;

    if (duration <= TimeRange.FETCH_DATA_DURATION) {
        timeRanges.add(new TimeRange(start, end));
    } else {
        long currentStart = start;
        while (currentStart < end) {
            long currentEnd = currentStart + TimeRange.FETCH_DATA_DURATION;
            if (currentEnd > end) {
                currentEnd = end;
            }
            timeRanges.add(new TimeRange(currentStart, currentEnd));
            currentStart = currentEnd;
        }
    }

    return timeRanges;
}
}
