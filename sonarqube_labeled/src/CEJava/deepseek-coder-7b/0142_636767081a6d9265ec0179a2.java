package generated;
public class Generatedaca1cb8da825 {
private static boolean isAllZeros(String s){
    if(s == null || s.isEmpty()){
        return true;
    }
    for(char c : s.toCharArray()){
        if(c != '0'){
            return false;
        }
    }
    return true;
}
}
