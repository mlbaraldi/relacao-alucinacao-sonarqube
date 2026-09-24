package generated;
public class Generated87c95d0b1997 {
@Override public int hashCode(){
    int result = 17;
    result = 31 * result + (int) (this.id ^ (this.id >>> 32));
    result = 31 * result + (this.name != null ? this.name.hashCode() : 0);
    result = 31 * result + (this.age != null ? this.age.hashCode() : 0);
    return result;
}
}
