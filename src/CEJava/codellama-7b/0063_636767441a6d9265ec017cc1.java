package generated;
public class Generated7f90cd933e83 {
private TreeNode<T> rotateRight(TreeNode<T> node){
    // Get the left child of the node
    TreeNode<T> leftChild = node.getLeft();

    // Set the left child's right child to the node's right child
    leftChild.setRight(node.getRight());

    // Set the node's right child to the left child
    node.setRight(leftChild);

    // Return the new parent of the node
    return leftChild;
}
}
