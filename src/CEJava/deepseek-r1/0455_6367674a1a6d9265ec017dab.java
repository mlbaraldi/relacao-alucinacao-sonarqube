package generated;
public class Generated311053e51b1b {
@Override public int compare(Double o1,Double o2){
    double d1 = o1;
    double d2 = o2;

    // Handle NaN cases
    if (Double.isNaN(d1)) {
        return Double.isNaN(d2) ? 0 : 1;
    }
    if (Double.isNaN(d2)) {
        return -1;
    }

    // Compare numerical values
    if (d1 < d2) {
        return -1;
    } else if (d1 > d2) {
        return 1;
    } else {
        // Check for 0.0 vs -0.0 by comparing their bit patterns
        long bits1 = Double.doubleToLongBits(d1);
        long bits2 = Double.doubleToLongBits(d2);
        if (bits1 == bits2) {
            return 0;
        } else {
            return bits1 < bits2 ? -1 : 1;
        }
    }
}
}
