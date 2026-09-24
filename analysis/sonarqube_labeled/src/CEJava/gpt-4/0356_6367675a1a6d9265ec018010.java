package generated;
public class Generatede4f8cd825828 {
void removeSelf(){
    if (this.next != null) {
        this.value = this.next.value;
        this.next = this.next.next;
    }
}
}
