package generated;
public class Generated163285eb6141 {
private void pop(final String descriptor){
    try {
        Class<?> clazz = Class.forName(descriptor);
        while (!outputFrameStack.isEmpty() && outputFrameStack.peek().getClass() == clazz) {
            outputFrameStack.pop();
        }
    } catch (ClassNotFoundException e) {
        e.printStackTrace();
    }
}
}
