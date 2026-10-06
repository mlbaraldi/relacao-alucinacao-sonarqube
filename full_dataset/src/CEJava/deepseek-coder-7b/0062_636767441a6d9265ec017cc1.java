package generated;
public class Generated7f90cd933e83 {
private TreeNode<T> rotateRight(TreeNode<T> node){
    TreeNode<T> newParent = node.left;
    node.left = newParent.right;
    newParent.right = node;
    return newParent;
}
}
