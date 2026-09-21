package generated;
public class Generatedfdac95e05b26 {
int visitFrameStart(final int offset,final int numLocal,final int numStack){
    // Create a new stack map frame
    StackMapFrame frame = new StackMapFrame(offset, numLocal, numStack);

    // Add the frame to the current frame list
    currentFrame = frame;

    // Return the index of the next element to be written in this frame
    return frame.getNextIndex();
}
}
