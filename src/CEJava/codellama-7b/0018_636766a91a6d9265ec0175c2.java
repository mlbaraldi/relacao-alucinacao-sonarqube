package generated;
public class Generated8841500f7ac2 {
private int pop(){
    if (outputFrameStack.isEmpty()) {
        throw new IllegalStateException("Output frame stack is empty");
    }
    int value = outputFrameStack.pop();
    return value;
}
}
