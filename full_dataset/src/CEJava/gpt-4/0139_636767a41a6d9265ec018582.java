package generated;
public class Generatede9e9a05899e0 {
public static <T>int writeDelimitedTo(OutputStream out,T message,Schema<T> schema,LinkedBuffer buffer) throws IOException {
    // Serialize the message to a byte array
    byte[] data = ProtostuffIOUtil.toByteArray(message, schema, buffer);

    // Write the length of the serialized data to the output stream
    out.write(data.length);

    // Write the serialized data to the output stream
    out.write(data);

    // Clear the buffer for reuse
    buffer.clear();

    // Return the size of the serialized data
    return data.length;
}
}
