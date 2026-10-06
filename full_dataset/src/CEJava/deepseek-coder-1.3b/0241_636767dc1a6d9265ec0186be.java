package generated;
public class Generated42957149847e {
static long compressTimeBucket(long timeBucket,int dayStep){
    long startOfDay = timeBucket / (1000 * 60 * 60 * 24) * (1000 * 60 * 60 * 24);
    long startOfNextDay = startOfDay + (1000 * 60 * 60 * 24) * dayStep;
    return startOfNextDay;
}
}
