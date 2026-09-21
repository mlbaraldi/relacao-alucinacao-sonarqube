package generated;
public class Generated8f87d4b5ad46 {
public static int nullSafeHashCode(long[] array){
    if (array == null) {
        return 0;
    }

    int hash = 1;
    for (long element : array) {
        hash = 31 * hash + (int) (element ^ (element >>> 32));
    }
    return hash;
}
}
