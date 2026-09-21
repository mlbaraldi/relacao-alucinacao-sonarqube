package generated;
public class Generated6a22b3742a3b {
public static byte[] toPrimitive(final Byte[] array){
    if(array == null){
        return null;
    }

    byte[] primitiveBytes = new byte[array.length];

    for(int i = 0; i < array.length; i++){
        primitiveBytes[i] = array[i];
    }

    return primitiveBytes;
}
}
