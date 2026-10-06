package generated;
public class Generatedc144031dd6a7 {
@Override public boolean containsKey(final Object key){
    for (Entry<K, V> entry : entrySet()) {
        if (Objects.equals(key, entry.getKey())) {
            return true;
        }
    }
    return false;
}
}
