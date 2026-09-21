package generated;
public class Generatedebd5aa4c1330 {
Edge edgeToNext(){
    Node startNode = currentNode.realNode != null ? currentNode.realNode : currentNode;
    Node endNode = nextNode.realNode != null ? nextNode.realNode : nextNode;

    return new Edge(startNode, endNode);
}
}
