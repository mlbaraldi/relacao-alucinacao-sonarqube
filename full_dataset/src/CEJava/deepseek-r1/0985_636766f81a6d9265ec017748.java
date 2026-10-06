package generated;
public class Generatedaf336a6bf556 {
public static String base64Decode(final String s){
    if (s == null) {
        return null;
    }

    int len = s.length();
    if (len % 4 != 0) {
        throw new IllegalArgumentException("Input string length must be a multiple of four.");
    }

    int numGroups = len / 4;
    if (numGroups == 0) {
        return "";
    }

    // Determine padding count in the last group
    String lastGroup = s.substring(len - 4);
    int paddingCount = 0;
    for (int i = 0; i < 4; i++) {
        if (lastGroup.charAt(i) == '=') {
            paddingCount++;
        } else {
            // Ensure remaining characters in the group are not padding
            for (int j = i + 1; j < 4; j++) {
                if (lastGroup.charAt(j) == '=') {
                    throw new IllegalArgumentException("Invalid padding in the last group.");
                }
            }
            break;
        }
    }

    if (paddingCount > 2) {
        throw new IllegalArgumentException("Too many padding characters in the last group.");
    }

    byte[] base64DecodeTable = new byte[256];
    Arrays.fill(base64DecodeTable, (byte) -1);
    String base64Chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
    for (int i = 0; i < base64Chars.length(); i++) {
        base64DecodeTable[base64Chars.charAt(i)] = (byte) i;
    }

    int totalBytes = (numGroups - 1) * 3 + (3 - paddingCount);
    byte[] result = new byte[totalBytes];
    int resultIndex = 0;

    for (int group = 0; group < numGroups; group++) {
        String currentGroup = s.substring(group * 4, group * 4 + 4);
        int[] sextets = new int[4];
        for (int i = 0; i < 4; i++) {
            char c = currentGroup.charAt(i);
            if (c == '=') {
                if (group != numGroups - 1) {
                    throw new IllegalArgumentException("Padding '=' found in non-last group.");
                }
                sextets[i] = 0;
            } else {
                byte val = base64DecodeTable[c];
                if (val == -1) {
                    throw new IllegalArgumentException("Invalid character in Base64 string: " + c);
                }
                sextets[i] = val;
            }
        }

        int combined = (sextets[0] << 18) | (sextets[1] << 12) | (sextets[2] << 6) | sextets[3];
        byte[] bytes = new byte[3];
        bytes[0] = (byte) ((combined >> 16) & 0xFF);
        bytes[1] = (byte) ((combined >> 8) & 0xFF);
        bytes[2] = (byte) (combined & 0xFF);

        int bytesToTake = (group == numGroups - 1) ? (3 - paddingCount) : 3;
        for (int i = 0; i < bytesToTake; i++) {
            result[resultIndex++] = bytes[i];
        }
    }

    try {
        return new String(result, "UTF-8");
    } catch (UnsupportedEncodingException e) {
        throw new RuntimeException("UTF-8 encoding not supported", e);
    }
}
}
