package generated;
public class Generatede9e9a05899e0 {
public static <T>int writeDelimitedTo(OutputStream out,T message,Schema<T> schema,LinkedBuffer buffer) throws IOException {
    // Serialize the message into the buffer to determine its size
    ProtobufOutput output = new ProtobufOutput(buffer);
    schema.writeTo(output, message);
    int messageSize = output.getSize();

    // Prepend the varint encoded message size to the buffer chain
    LinkedBuffer varintBuffer = ProtobufOutput.writeRawVarInt32Bytes(messageSize, buffer);

    // Write the entire buffer chain (varint + message) to the output stream
    LinkedBuffer.writeTo(out, varintBuffer);

    // Return the size of the message (excluding the varint prefix)
    return messageSize;
}
}
