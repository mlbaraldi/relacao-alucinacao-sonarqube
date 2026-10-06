package generated;
public class Generated02ed7a14f3d0 {
public static boolean equals(Point2D p1,Point2D p2){
    final double TOLERANCE = 1e-9;
    return Math.abs(p1.getX() - p2.getX()) < TOLERANCE && Math.abs(p1.getY() - p2.getY()) < TOLERANCE;
}
}
