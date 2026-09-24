package generated;
public class Generatede4f8cd825828 {
void removeSelf(){
    if (prev) {
        prev->next = next;
    }
    if (next) {
        next->prev = prev;
    }
    prev = nullptr;
    next = nullptr;
}
}
