package generated;
public class Generated8b0123611be9 {
public void putAllWriteable(BeanMap map){
    try {
        Map<String, Object> otherMap = BeanUtils.describe(other);
        for (Map.Entry<String, Object> entry : otherMap.entrySet()) {
            if (!entry.getKey().equals("class")) { // Ignore class property
                map.put(entry.getKey(), entry.getValue());
            }
        }
    } catch (IllegalAccessException | InvocationTargetException e) {
        e.printStackTrace();
    }
}
}
