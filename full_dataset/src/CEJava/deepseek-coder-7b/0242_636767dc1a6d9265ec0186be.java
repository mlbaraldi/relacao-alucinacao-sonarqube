package generated;
public class Generated42957149847e {
static long compressTimeBucket(long timeBucket,int dayStep){
    if (timeBucket >= dayStep) {
        return timeBucket - dayStep;
    } else {
        return timeBucket;
    }
}
}
