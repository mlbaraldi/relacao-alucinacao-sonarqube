package generated;
public class Generated7c9748f01d95 {
protected List<TimeRange> buildTimeRanges(long start,long end){
    List<TimeRange> timeRanges = new ArrayList<>();
    long duration = FETCH_DATA_DURATION;
    long startTime = start;
    long endTime = start + duration;
    while (endTime <= end) {
        timeRanges.add(new TimeRange(startTime, endTime));
        startTime = endTime;
        endTime = startTime + duration;
    }
    return timeRanges;
}
}
