package generated;
public class Generated2a86da12dcd8 {
protected int removeUnusedNodes(){
    int numRemoved = 0;
    for (CategoryNode node : categoryTree) {
        if (!node.isActive()) {
            categoryTree.remove(node);
            numRemoved++;
        }
    }
    return numRemoved;
}
}
