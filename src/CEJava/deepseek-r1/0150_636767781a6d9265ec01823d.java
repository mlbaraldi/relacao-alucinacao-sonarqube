package generated;
public class Generated10b3e2f27a4d {
protected void subAppend(LoggingEvent event){
    if (layout == null) {
        errorHandler.error("No layout set for the appender.", null, ErrorCode.MISSING_LAYOUT);
        return;
    }

    String formattedMessage = layout.format(event);

    if (writer == null) {
        errorHandler.error("No output writer configured.", null, ErrorCode.WRITER_FAILURE);
        return;
    }

    try {
        writer.write(formattedMessage);
        if (immediateFlush) {
            writer.flush();
        }
    } catch (IOException e) {
        errorHandler.error("Failed to write log event.", e, ErrorCode.WRITE_FAILURE);
    }
}
}
