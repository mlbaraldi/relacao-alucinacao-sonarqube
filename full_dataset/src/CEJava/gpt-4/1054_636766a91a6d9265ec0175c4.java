package generated;
public class Generated163285eb6141 {
private void pop(final String descriptor){
    // Assuming that the stack is a member variable of the class
    for (int i = 0; i < descriptor.length(); i++) {
        // Check if the stack is not empty before popping
        if (!outputFrameStack.isEmpty()) {
            outputFrameStack.pop();
        } else {
            throw new IllegalStateException("Trying to pop from an empty stack");
        }
    }
}
}
