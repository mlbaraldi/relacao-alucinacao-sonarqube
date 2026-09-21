package generated;
public class Generated82d678fbe6a9 {
public static boolean isDigits(String str){
    if(str == null || str.isEmpty()){
        return false;
    }
    for(int i = 0; i < str.length(); i++){
        if(!Character.isDigit(str.charAt(i))){
            return false;
        }
    }
    return true;
}
}
