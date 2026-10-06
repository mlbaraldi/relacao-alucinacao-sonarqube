package generated;
public class Generatedbd1ad46c1b75 {
public static Character toCharacterObject(final char ch){
    if (ch < 128) {
        return CharacterCache.get(ch);
    } else {
        return new Character(ch);
    }
}
}
