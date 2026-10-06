package generated;
public class Generated163285eb6141 {
private void pop(final String descriptor){
    // Get the number of abstract types to pop from the output frame stack
    int numTypesToPop = getNumTypesToPop(descriptor);

    // Pop the abstract types from the output frame stack
    for (int i = 0; i < numTypesToPop; i++) {
        outputFrameStack.pop();
    }
}
}
