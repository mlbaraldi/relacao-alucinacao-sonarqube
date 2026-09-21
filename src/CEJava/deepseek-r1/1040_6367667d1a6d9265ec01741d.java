package generated;
public class Generated1f5a5c0e7b0c {
public static Type resolveBound(TypeVariable<?> typeVariable){
    Type[] bounds = typeVariable.getBounds();
    return bounds.length > 0 ? bounds[0] : Unknown.class;
}
}
