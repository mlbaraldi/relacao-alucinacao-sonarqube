package generated;
public class Generateda4c4ba3e2bdb {
private void checkIfPackedField() throws IOException {
    // Check if the current wire type is length-delimited
    if (getWireType() != WireFormat.WIRETYPE_LENGTH_DELIMITED) {
        return;
    }

    // Retrieve the current field descriptor; if not packed, return
    FieldDescriptor field = this.fieldDescriptor;
    if (field == null || !field.isPacked()) {
        return;
    }

    // Read the length of the packed data
    int length = input.readRawVarint32();

    // Push the new limit onto the input stream
    input.pushLimit(length);

    // Update internal state to indicate processing a packed field
    this.packedDepth++;
}
}
