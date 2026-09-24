package generated;
public class Generated8f87d4b5ad46 {
public static int nullSafeHashCode(long[] array){
    if (array == null) {
        return 0;
    }
    int result = 1;
    for (long element : array) {
        int elementHash = (int)(element ^ (element >>> 32));
        result = 31 * result + elementHash;
    }
    return result;
}
}
