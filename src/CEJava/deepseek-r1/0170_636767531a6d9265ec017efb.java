package generated;
public class Generatedc315db42d989 {
void insertBefore(Bucket bucket){
    this.next = bucket;
    this.previous = bucket.previous;

    if (bucket.previous != null) {
        bucket.previous.next = this;
    }

    bucket.previous = this;
}
}
