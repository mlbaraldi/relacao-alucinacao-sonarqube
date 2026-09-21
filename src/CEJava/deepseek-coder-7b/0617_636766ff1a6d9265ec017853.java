package generated;
public class Generatedec0778698db5 {
protected Label readLabel(final int bytecodeOffset,final Label[] labels){
    // Check if a label already exists for the given bytecode offset
    if (labels[bytecodeOffset] == null) {
        // If not, create a new label and store it in the labels array
        labels[bytecodeOffset] = new Label();
    }
    // Return the label at the given bytecode offset
    return labels[bytecodeOffset];
}
}
