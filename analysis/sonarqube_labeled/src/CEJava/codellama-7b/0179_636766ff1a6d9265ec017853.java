package generated;
public class Generatedec0778698db5 {
protected Label readLabel(final int bytecodeOffset,final Label[] labels){
    // Check if a label already exists for the given bytecode offset
    if (labels[bytecodeOffset] != null) {
        return labels[bytecodeOffset];
    }

    // Create a new label for the given bytecode offset
    Label label = new Label();
    label.setOffset(bytecodeOffset);
    labels[bytecodeOffset] = label;
    return label;
}
}
