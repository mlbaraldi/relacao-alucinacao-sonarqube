package generated;
public class Generated299ec356cfd9 {
public boolean isCompatible(DataTable dataset){
    if (dataset == null) {
        return false;
    }
    Bucket otherBucket = dataset.getBucket();
    if (otherBucket == null) {
        return false;
    }
    if (this.getColumns().size() != otherBucket.getColumns().size()) {
        return false;
    }
    for (int i = 0; i < this.getColumns().size(); i++) {
        Column thisCol = this.getColumns().get(i);
        Column otherCol = otherBucket.getColumns().get(i);
        if (!thisCol.getName().equals(otherCol.getName())) {
            return false;
        }
        if (!thisCol.getType().equals(otherCol.getType())) {
            return false;
        }
    }
    return true;
}
}
