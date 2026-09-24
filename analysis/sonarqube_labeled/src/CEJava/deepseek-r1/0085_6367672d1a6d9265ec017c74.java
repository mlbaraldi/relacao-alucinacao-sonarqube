package generated;
public class Generatedcedd30ff7ec1 {
public boolean remove(int val){
    for (int i = 0; i < elements.size(); i++) {
        if (elements.get(i) == val) {
            elements.remove(i);
            return true;
        }
    }
    return false;
}
}
