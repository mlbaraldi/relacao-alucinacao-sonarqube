package generated;
public class Generated5e0ca9c679fb {
public static Pair<Box2D,Box2D> splitAlongXAxis(Box2D box){
    // Calculate the new width for the split boxes
    float newWidth = box.getWidth() / 2;

    // Create the first box starting from the same origin and with half the width
    Box2D box1 = new Box2D(box.getOrigin(), new Vector2(newWidth, box.getHeight()));

    // Create the second box starting from the middle of the original box and with half the width
    Vector2 newOrigin = new Vector2(box.getOrigin().getX() + newWidth, box.getOrigin().getY());
    Box2D box2 = new Box2D(newOrigin, new Vector2(newWidth, box.getHeight()));

    // Return the pair of boxes
    return new Pair<>(box1, box2);
}
}
