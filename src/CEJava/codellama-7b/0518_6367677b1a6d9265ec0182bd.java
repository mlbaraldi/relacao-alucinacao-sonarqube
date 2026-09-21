package generated;
public class Generated601f27adee4b {
public String format(final LoggingEvent event){
    StringBuilder builder = new StringBuilder();
    builder.append(event.getLevel().getName());
    builder.append(" - ");
    builder.append(event.getMessage());
    builder.append(" (");
    builder.append(event.getThreadName());
    builder.append(")");
    return builder.toString();
}
}
