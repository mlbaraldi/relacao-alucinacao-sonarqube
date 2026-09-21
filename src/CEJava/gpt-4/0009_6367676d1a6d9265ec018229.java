package generated;
public class Generated0cd6c9efe8f9 {
public static String[] trimArrayElements(String[] array){
    if(array == null) {
        return null;
    }
    for(int i = 0; i < array.length; i++){
        if(array[i] != null) {
            array[i] = array[i].trim();
        }
    }
    return array;
}
}
