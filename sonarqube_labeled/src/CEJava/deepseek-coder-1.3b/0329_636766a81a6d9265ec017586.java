package generated;
public class Generatedba9fc61459e9 {
private void pop(final int elements){
    // Create a temporary stack to hold the popped elements
    Stack<AbstractType> tempStack = new Stack<>();

    // Pop elements from the output frame stack until it's empty or the desired number of elements is popped
    while(!outputFrameStack.isEmpty() && elements > 0){
        AbstractType element = outputFrameStack.pop();
        tempStack.push(element);
        elements--;
    }

    // If there are still elements in the output frame stack, clear it
    if(!outputFrameStack.isEmpty()){
        outputFrameStack.clear();
    }

    // Push the popped elements back to the output frame stack
    while(!tempStack.isEmpty()){
        outputFrameStack.push(tempStack.pop());
    }
}
}
