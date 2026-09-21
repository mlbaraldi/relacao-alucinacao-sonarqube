package generated;
public class Generatedba9fc61459e9 {
private void pop(final int elements){
    for (int i = 0; i < elements; i++) {
        if (!outputFrameStack.isEmpty()) {
            outputFrameStack.pop();
        } else {
            System.out.println("The stack is already empty. No more elements can be popped.");
            break;
        }
    }
}
}
