package generated;
public class Generated82d678fbe6a9 {
public static boolean isDigits(String str){
    if(str == null || str.isEmpty()){
        return false;
    }
    for(char c : str.toCharArray()){
        if(!Character.isDigit(c) && c != '.'){
            return false;
        }
    }
    return true;
}
}
