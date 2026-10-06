package generated;
public class Generated5b920ecd3f5a {
public String toString(){
    if(queue.isEmpty()) {
        return "[]";
    }

    StringBuilder sb = new StringBuilder();
    sb.append('[');

    for(Object item : queue) {
        sb.append(item.toString());
        sb.append(", ");
    }

    sb.delete(sb.length()-2, sb.length());
    sb.append(']');

    return sb.toString();
}
}
