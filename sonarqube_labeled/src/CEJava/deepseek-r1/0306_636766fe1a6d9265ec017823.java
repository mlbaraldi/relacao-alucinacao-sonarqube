package generated;
public class Generated9f37ef8ceeb6 {
int addConstantNameAndType(final String name,final String descriptor){
    // Step 1: Add name and descriptor as Utf8 constants and get their indices
    int nameIndex = addConstantUtf8(name);
    int descriptorIndex = addConstantUtf8(descriptor);
    
    // Step 2: Compute hash code for the NameAndType entry
    int hashCode = 0x7FFFFFFF & (Constants.NAMEANDTYPE + nameIndex * 33 + descriptorIndex * 7);
    int bucket = hashCode % table.length;
    
    // Step 3: Check existing entries in the bucket for a match
    Item item = table[bucket];
    while (item != null) {
        if (item.tag == Constants.NAMEANDTYPE && 
            item.nameIndex == nameIndex && 
            item.descriptorIndex == descriptorIndex) {
            return item.index; // Existing entry found, return its index
        }
        item = item.next;
    }
    
    // Step 4: Create and add new entry if not found
    Item newItem = new Item();
    newItem.tag = Constants.NAMEANDTYPE;
    newItem.nameIndex = nameIndex;
    newItem.descriptorIndex = descriptorIndex;
    newItem.hashCode = hashCode;
    newItem.index = constantPoolCount++;
    
    // Insert the new item into the hash table
    newItem.next = table[bucket];
    table[bucket] = newItem;
    
    return newItem.index;
}
}
