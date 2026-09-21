package generated;
public class Generateda2522b2dfe92 {
public void overrideName(String oldName,String newName){
    // Check if the old name is valid
    if (oldName == null || oldName.isEmpty()) {
        throw new IllegalArgumentException("Old name cannot be null or empty");
    }

    // Check if the new name is valid
    if (newName == null || newName.isEmpty()) {
        throw new IllegalArgumentException("New name cannot be null or empty");
    }

    // Replace the old name with the new name in the storage level
    storageLevel.replace(oldName, newName);
}
}
