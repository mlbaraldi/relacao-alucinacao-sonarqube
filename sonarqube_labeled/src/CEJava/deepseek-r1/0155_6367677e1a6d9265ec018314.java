package generated;
public class Generated2a86da12dcd8 {
protected int removeUnusedNodes(){
    List<Category> inactiveNodes = new ArrayList<>();
    Map<Category, Integer> nodeDepths = new HashMap<>();

    // Traverse the tree to collect inactive nodes and their depths
    traverseTree(root, 0, inactiveNodes, nodeDepths);

    // Sort the inactive nodes by depth in descending order to process deepest nodes first
    inactiveNodes.sort((a, b) -> Integer.compare(nodeDepths.get(b), nodeDepths.get(a)));

    int count = 0;
    for (Category node : inactiveNodes) {
        Category parent = node.getParent();
        if (parent != null) {
            // Remove the node from its parent's children list
            parent.getChildren().remove(node);

            // Get the node's children and add them to the parent's children list
            List<Category> children = node.getChildren();
            parent.getChildren().addAll(children);

            // Update the parent of each child to the current node's parent
            for (Category child : children) {
                child.setParent(parent);
            }

            count++;
        }
        // If parent is null (root node), do nothing as we cannot remove the root
    }

    return count;
}
}
