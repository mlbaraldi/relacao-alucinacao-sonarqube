package generated;
public class Generatede68949d37df1 {
public void addMessage(final LogRecord lr){
    SwingUtilities.invokeLater(new Runnable() {
        @Override
        public void run() {
            // Here you would add the log record to the LogTable
            // This is just a placeholder, replace with actual code
            System.out.println("Adding log record: " + lr.getMessage());
        }
    });
}
}
