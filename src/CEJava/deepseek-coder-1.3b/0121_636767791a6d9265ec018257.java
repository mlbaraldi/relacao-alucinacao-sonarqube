package generated;
public class Generatede68949d37df1 {
public void addMessage(final LogRecord lr){
    SwingUtilities.invokeLater(new Runnable() {
        public void run() {
            synchronized (lock) {
                logRecords.add(lr);
                // Update your LogTable here
            }
        }
    });
}
}
