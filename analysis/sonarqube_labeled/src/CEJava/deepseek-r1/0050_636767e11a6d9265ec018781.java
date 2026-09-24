package generated;
public class Generated71b03dbc71b6 {
@Override public void accept(final METRICS data){
    if (data == null) {
        return;
    }
    if (currentMetrics == null) {
        currentMetrics = data;
    } else {
        currentMetrics.merge(data);
    }
}
}
