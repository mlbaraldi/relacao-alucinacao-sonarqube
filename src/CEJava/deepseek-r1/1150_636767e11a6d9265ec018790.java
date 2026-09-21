package generated;
public class Generatedf355ae4851b3 {
public static List<ThreadSnapshot> parseFromFileWithTimeRange(File file,List<ProfileAnalyzeTimeRange> timeRanges) throws IOException {
    List<ThreadSnapshot> result = new ArrayList<>();

    try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(file))) {
        while (true) {
            try {
                ThreadSnapshot snapshot = (ThreadSnapshot) ois.readObject();
                long timestamp = snapshot.getTimestamp();
                for (ProfileAnalyzeTimeRange range : timeRanges) {
                    if (timestamp >= range.getStartTime() && timestamp <= range.getEndTime()) {
                        result.add(snapshot);
                        break;
                    }
                }
            } catch (EOFException e) {
                // End of file reached
                break;
            } catch (ClassNotFoundException e) {
                throw new IOException("Class not found during deserialization", e);
            }
        }
    }

    return result;
}
}
