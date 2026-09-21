package generated;
public class Generated3d11c8e2ae7e {
public void removeFromTreeEdgeList(){
    // Handle the first doubly linked list
    if (prevTree1 != null) {
        prevTree1.nextTree1 = nextTree1;
    }
    if (nextTree1 != null) {
        nextTree1.prevTree1 = prevTree1;
    }
    prevTree1 = null;
    nextTree1 = null;

    // Handle the second doubly linked list
    if (prevTree2 != null) {
        prevTree2.nextTree2 = nextTree2;
    }
    if (nextTree2 != null) {
        nextTree2.prevTree2 = prevTree2;
    }
    prevTree2 = null;
    nextTree2 = null;
}
}
