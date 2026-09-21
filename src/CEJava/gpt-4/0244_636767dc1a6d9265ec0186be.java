package generated;
public class Generated42957149847e {
static long compressTimeBucket(long timeBucket,int dayStep){
    // Extract the year, month, and day from the timeBucket
    long year = timeBucket / 10000;
    long month = (timeBucket % 10000) / 100;
    long day = timeBucket % 100;

    // Calculate the new day
    long newDay = ((day - 1) / dayStep) * dayStep + 1;

    // Combine the year, month, and new day into a new timeBucket
    long newTimeBucket = year * 10000 + month * 100 + newDay;

    return newTimeBucket;
}
}
