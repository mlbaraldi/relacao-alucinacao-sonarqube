package generated;
public class Generated5217f864e17f {
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
