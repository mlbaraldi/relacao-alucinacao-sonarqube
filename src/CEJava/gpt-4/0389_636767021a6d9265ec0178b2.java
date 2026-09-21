package generated;
public class Generated5217f864e17f {
private void pop(final String descriptor){
    // Assuming that the stack is a member variable of the class
    for (int i = 0; i < descriptor.length(); i++) {
        // Check if the stack is not empty before popping
        if (!stack.isEmpty()) {
            stack.pop();
        } else {
            throw new IllegalStateException("Stack is empty, cannot pop more elements");
        }
    }
}
}
