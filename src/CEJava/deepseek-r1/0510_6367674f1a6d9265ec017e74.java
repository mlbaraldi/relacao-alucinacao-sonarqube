package generated;
public class Generated5b920ecd3f5a {
public String toString(){
    StringBuilder sb = new StringBuilder("[");
    Iterator<E> it = iterator();
    boolean first = true;
    while (it.hasNext()) {
        E element = it.next();
        if (first) {
            first = false;
        } else {
            sb.append(", ");
        }
        sb.append(element);
    }
    sb.append("]");
    return sb.toString();
}
}
