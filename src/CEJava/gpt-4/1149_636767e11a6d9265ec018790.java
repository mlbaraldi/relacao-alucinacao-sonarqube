package generated;
public class Generatedf355ae4851b3 {
public static List<ThreadSnapshot> parseFromFileWithTimeRange(File file,List<ProfileAnalyzeTimeRange> timeRanges) throws IOException {
    List<ThreadSnapshot> snapshots = new ArrayList<>();
    try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(file))) {
        while (true) {
            try {
                ThreadSnapshot snapshot = (ThreadSnapshot) ois.readObject();
                for (ProfileAnalyzeTimeRange range : timeRanges) {
                    if (snapshot.getTime().after(range.getStartTime()) && snapshot.getTime().before(range.getEndTime())) {
                        snapshots.add(snapshot);
                        break;
                    }
                }
            } catch (EOFException e) {
                break;
            } catch (ClassNotFoundException e) {
                throw new IOException("Class not found", e);
            }
        }
    }
    return snapshots;
}
}
