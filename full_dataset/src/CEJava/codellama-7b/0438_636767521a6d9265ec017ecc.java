package generated;
public class Generated5e0ca9c679fb {
public static Pair<Box2D,Box2D> splitAlongXAxis(Box2D box){
    // Calculate the midpoint of the box along the x-axis
    double midpointX = box.getMinX() + (box.getMaxX() - box.getMinX()) / 2;

    // Create two new boxes, one with the left half of the original box and the other with the right half
    Box2D leftBox = new Box2D(box.getMinX(), midpointX, box.getMinY(), box.getMaxY());
    Box2D rightBox = new Box2D(midpointX, box.getMaxX(), box.getMinY(), box.getMaxY());

    // Return a pair with the two resulting boxes
    return new Pair<>(leftBox, rightBox);
}
}
