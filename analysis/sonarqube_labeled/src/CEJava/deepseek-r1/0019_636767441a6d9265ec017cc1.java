package generated;
public class Generated7f90cd933e83 {
private TreeNode<T> rotateRight(TreeNode<T> node){
    TreeNode<T> leftChild = node.left;
    TreeNode<T> temp = leftChild.right;
    leftChild.right = node;
    node.left = temp;
    return leftChild;
}
}
