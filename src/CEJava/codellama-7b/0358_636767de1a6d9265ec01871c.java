package generated;
public class Generatedb54f4edc7765 {
public void valueAccumulation(String key,Long value){
    // Get the current value for the given key
    Long currentValue = map.get(key);

    // If the key is not present in the map, set the value to the given value
    if (currentValue == null) {
        map.put(key, value);
    } else {
        // Otherwise, accumulate the value with the existing value
        map.put(key, currentValue + value);
    }
}
}
