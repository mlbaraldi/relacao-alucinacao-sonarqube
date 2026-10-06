package generated;
public class Generated163285eb6141 {
private void pop(final String descriptor){
    int popCount = 0;
    if (descriptor.charAt(0) == '(') {
        Type[] argumentTypes = Type.getArgumentTypes(descriptor);
        for (Type argType : argumentTypes) {
            popCount += argType.getSize();
        }
    } else {
        Type type = Type.getType(descriptor);
        popCount = type.getSize();
    }
    // Assuming outputFrame is a List<Object> representing the stack
    int stackSize = outputFrame.size();
    outputFrame.subList(stackSize - popCount, stackSize).clear();
}
}
