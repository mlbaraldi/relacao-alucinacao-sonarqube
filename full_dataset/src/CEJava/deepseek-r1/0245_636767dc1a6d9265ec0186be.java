package generated;
public class Generated42957149847e {
static long compressTimeBucket(long timeBucket,int dayStep){
    // Convert timeBucket to an 8-digit string with leading zeros if necessary
    String tbStr = String.format("%08d", timeBucket);
    int year = Integer.parseInt(tbStr.substring(0, 4));
    int month = Integer.parseInt(tbStr.substring(4, 6));
    int day = Integer.parseInt(tbStr.substring(6, 8));
    
    // Calculate the new day using the dayStep
    int newDay = ((day - 1) / dayStep) * dayStep + 1;
    
    // Format the new time bucket string and convert back to long
    String newTbStr = String.format("%04d%02d%02d", year, month, newDay);
    return Long.parseLong(newTbStr);
}
}
