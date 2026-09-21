package generated;
public class Generated02ed7a14f3d0 {
public static boolean equals(Point2D p1,Point2D p2){
    if (p1 == p2) {
        return true;
    }
    if (p1 == null || p2 == null) {
        return false;
    }
    double dx = p1.getX() - p2.getX();
    double dy = p1.getY() - p2.getY();
    return Math.abs(dx) <= 1e-9 && Math.abs(dy) <= 1e-9;
}
}
