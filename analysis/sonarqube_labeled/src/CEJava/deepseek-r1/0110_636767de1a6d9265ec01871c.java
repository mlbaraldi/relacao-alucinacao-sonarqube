package generated;
public class Generatedb54f4edc7765 {
public void valueAccumulation(String key,Long value){
    Long safeValue = (value != null) ? value : 0L;
    accumulatorMap.merge(key, safeValue, (oldVal, newVal) -> oldVal + newVal);
}
}
