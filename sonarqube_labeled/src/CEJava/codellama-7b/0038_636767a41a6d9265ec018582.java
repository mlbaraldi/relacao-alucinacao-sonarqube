package generated;
public class Generatede9e9a05899e0 {
public static <T>int writeDelimitedTo(OutputStream out,T message,Schema<T> schema,LinkedBuffer buffer) throws IOException {
    // Serialize the message using the schema
    byte[] serializedMessage = schema.serialize(message);

    // Write the length of the message to the output stream
    out.writeInt(serializedMessage.length);

    // Write the serialized message to the output stream
    out.write(serializedMessage);

    // Return the size of the message
    return serializedMessage.length;
}
}
