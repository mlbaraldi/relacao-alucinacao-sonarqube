package generated;
public class Generated2a86da12dcd8 {
protected int removeUnusedNodes(){
    int count = 0;
    // Assuming that Category class has a method isActive() to check if the node is active
    // and a method getChildren() to get the children of the node.
    for (Category category : categories) {
        if (!category.isActive() || category.getChildren().isEmpty()) {
            categories.remove(category);
            count++;
        }
    }
    return count;
}
}
