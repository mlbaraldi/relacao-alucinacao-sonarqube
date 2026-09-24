package generated;
public class Generated5217f864e17f {
private void pop(final String descriptor){
    int totalPop = 0;

    if (descriptor.startsWith("(")) {
        // Method descriptor: process arguments
        int end = descriptor.indexOf(')');
        if (end == -1) {
            throw new IllegalArgumentException("Invalid method descriptor: missing closing ')'");
        }
        String argsPart = descriptor.substring(1, end);
        int index = 0;
        while (index < argsPart.length()) {
            int arrayDimensions = 0;
            while (index < argsPart.length() && argsPart.charAt(index) == '[') {
                arrayDimensions++;
                index++;
            }

            if (arrayDimensions > 0) {
                // Array type, size is 1
                totalPop += 1;
                if (index >= argsPart.length()) break;
                char c = argsPart.charAt(index);
                if (c == 'L') {
                    int semiIndex = argsPart.indexOf(';', index);
                    if (semiIndex == -1) {
                        throw new IllegalArgumentException("Invalid descriptor in array type");
                    }
                    index = semiIndex + 1;
                } else {
                    index++;
                }
            } else {
                char c = argsPart.charAt(index);
                if (c == 'L') {
                    int semiIndex = argsPart.indexOf(';', index);
                    if (semiIndex == -1) {
                        throw new IllegalArgumentException("Invalid object type descriptor");
                    }
                    index = semiIndex + 1;
                    totalPop += 1;
                } else if (c == 'J' || c == 'D') {
                    totalPop += 2;
                    index++;
                } else {
                    totalPop += 1;
                    index++;
                }
            }
        }
    } else {
        // Type descriptor
        int arrayDimensions = 0;
        int index = 0;
        while (index < descriptor.length() && descriptor.charAt(index) == '[') {
            arrayDimensions++;
            index++;
        }

        if (arrayDimensions > 0) {
            totalPop = 1;
        } else {
            char c = descriptor.charAt(index);
            if (c == 'J' || c == 'D') {
                totalPop = 2;
            } else {
                totalPop = 1;
            }
        }
    }

    // Pop the calculated number of elements from the output frame stack
    while (totalPop > 0) {
        outputFrameStack.pop();
        totalPop--;
    }
}
}
