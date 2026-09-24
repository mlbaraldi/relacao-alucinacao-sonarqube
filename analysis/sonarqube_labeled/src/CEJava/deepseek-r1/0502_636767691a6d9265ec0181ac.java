package generated;
public class Generated2ce65cd9c4a0 {
public static String applyRelativePath(String path,String relativePath){
    if (relativePath.startsWith("/")) {
        return relativePath;
    }

    boolean isAbsolute = path.startsWith("/");
    List<String> components = new ArrayList<>();

    if (isAbsolute) {
        components.add("");
        String[] split = path.split("/+");
        for (String s : split) {
            if (s.isEmpty() && components.size() == 1) {
                continue;
            }
            components.add(s);
        }
    } else {
        String[] split = path.split("/+");
        for (String s : split) {
            components.add(s);
        }
    }

    String[] relSplit = relativePath.split("/+");
    for (String part : relSplit) {
        if (part.isEmpty()) {
            continue;
        }
        if (part.equals(".")) {
            continue;
        } else if (part.equals("..")) {
            if (isAbsolute) {
                if (components.size() > 1) {
                    components.remove(components.size() - 1);
                }
            } else {
                if (!components.isEmpty() && !components.get(components.size() - 1).equals("..")) {
                    components.remove(components.size() - 1);
                } else {
                    components.add("..");
                }
            }
        } else {
            components.add(part);
        }
    }

    if (components.isEmpty()) {
        return "";
    }

    StringBuilder result = new StringBuilder();
    for (int i = 0; i < components.size(); i++) {
        String s = components.get(i);
        if (i == 0 && isAbsolute) {
            result.append("/");
            if (s.isEmpty()) {
                continue;
            }
        }
        if (i > 0) {
            result.append("/");
        }
        result.append(s);
    }

    return result.toString();
}
}
