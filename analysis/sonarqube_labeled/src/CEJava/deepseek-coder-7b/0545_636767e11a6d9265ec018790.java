package generated;
public class Generatedf355ae4851b3 {
public static List<ThreadSnapshot> parseFromFileWithTimeRange(File file,List<ProfileAnalyzeTimeRange> timeRanges) throws IOException {
    List<ThreadSnapshot> snapshots = new ArrayList<>();

    try (BufferedReader br = new BufferedReader(new FileReader(file))) {
        String line;
        while ((line = br.readLine()) != null) {
            // Assuming the line contains a timestamp and the rest is the snapshot data
            String[] parts = line.split("\\s+");
            if (parts.length > 0) {
                LocalDateTime timestamp = LocalDateTime.parse(parts[0]);
                ThreadSnapshot snapshot = new ThreadSnapshot(timestamp, parts[1]); // Assuming the snapshot data starts from the second part
                snapshots.add(snapshot);
            }
        }
    }

    List<ThreadSnapshot> filteredSnapshots = new ArrayList<>();
    for (ProfileAnalyzeTimeRange timeRange : timeRanges) {
        for (ThreadSnapshot snapshot : snapshots) {
            if (snapshot.getTimestamp().isAfter(timeRange.getStart()) && snapshot.getTimestamp().isBefore(timeRange.getEnd())) {
                filtered
}
