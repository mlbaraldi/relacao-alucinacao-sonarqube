package generated;
public class Generated2a86da12dcd8 {
protected int removeUnusedNodes(){
    if (node == null) {
        return 0;
    }

    int removedNodes = 0;

    for (Iterator<Node> iterator = node.getChildren().iterator(); iterator.hasNext();) {
        Node child = iterator.next();
        if (!child.isActive()) {
            iterator.remove();
            removedNodes++;
        } else {
            removedNodes += removeUnusedNodes(child);
        }
    }

    return removedNodes;
}
}
