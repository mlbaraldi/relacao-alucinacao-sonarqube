package generated;
public class Generated5217f864e17f {
private void pop(final String descriptor){
    // Get the number of abstract types to pop from the output frame stack
    int numTypesToPop = getNumTypesToPop(descriptor);

    // Pop the abstract types from the output frame stack
    for (int i = 0; i < numTypesToPop; i++) {
        outputFrameStack.pop();
    }
}
}
