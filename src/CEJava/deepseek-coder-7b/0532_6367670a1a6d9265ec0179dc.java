package generated;
public class Generatedf48ed4ba2bab {
private void putAbstractTypes(final int start,final int end){
    if (start < 0 || start >= currentFrame.length) {
        throw new IllegalArgumentException("Start index is out of bounds");
    }
    if (end <= start || end > currentFrame.length) {
        throw new IllegalArgumentException("End index is out of bounds");
    }

    for (int i = start; i < end; i++) {
        int abstractType = currentFrame[i];
        stackMapTableEntries.add(abstractType);
    }
}
}
