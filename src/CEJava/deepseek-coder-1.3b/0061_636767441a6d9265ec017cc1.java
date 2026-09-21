package generated;
public class Generated7f90cd933e83 {
private TreeNode<T> rotateRight(TreeNode<T> node){
    if (node == null || node.left == null) {
        throw new IllegalArgumentException("Node must have at least one child");
    }

    TreeNode<T> newParent = node.left;
    TreeNode<T> oldLeft = node.left;

    // Point the left child of the new parent to the right child of the old left child
    newParent.right = oldLeft;

    // Point the right child of the old left child to the old parent
    oldLeft.right = node;

    // Point the old parent to the new parent
    node.left = newParent;

    return newParent;
}
}
