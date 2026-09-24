package generated;
public class Generatedf355ae4851b3 {
public static List<ThreadSnapshot> parseFromFileWithTimeRange(File file,List<ProfileAnalyzeTimeRange> timeRanges) throws IOException {
    List<ThreadSnapshot> threadSnapshots = new ArrayList<>();

    // Open the file for reading
    BufferedReader reader = new BufferedReader(new FileReader(file));

    // Read the file line by line
    String line;
    while ((line = reader.readLine()) != null) {
        // Check if the line contains a time range
        if (line.contains("TimeRange")) {
            // Extract the time range from the line
            String[] timeRangeParts = line.split(":");
            ProfileAnalyzeTimeRange timeRange = new ProfileAnalyzeTimeRange(
                Long.parseLong(timeRangeParts[1]),
                Long.parseLong(timeRangeParts[2])
            );

            // Check if the time range is within the specified time ranges
            if (timeRanges.contains(timeRange)) {
                // Parse the thread snapshot from the line
                ThreadSnapshot threadSnapshot = parseThreadSnapshot(line);
                threadSnapshots.add(threadSnapshot);
            }
        }
    }

    // Close the file
    reader.close();

    return threadSnapshots;
}
}
