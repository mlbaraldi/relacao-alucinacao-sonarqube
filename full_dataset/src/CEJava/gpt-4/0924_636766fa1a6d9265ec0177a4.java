package generated;
public class Generated10058f865448 {
public static Double[] toObject(final double[] array){
    if(array == null){
        return null;
    }
    Double[] result = new Double[array.length];
    for(int i = 0; i < array.length; i++){
        result[i] = Double.valueOf(array[i]);
    }
    return result;
}
}
