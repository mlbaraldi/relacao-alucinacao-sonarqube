package generated;
public class Generateda88d9e239d01 {
final void addLineNumber(final int lineNumber){
    if (lineNumber <= 0) {
        throw new IllegalArgumentException("Line number must be strictly positive");
    }
    this.lineNumbers.put(this.lineNumbers.size() + 1, lineNumber);
}
}
