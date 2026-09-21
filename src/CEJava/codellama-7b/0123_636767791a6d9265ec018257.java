package generated;
public class Generatede68949d37df1 {
public void addMessage(final LogRecord lr){
    SwingUtilities.invokeLater(new Runnable() {
        @Override
        public void run() {
            LogTable logTable = getLogTable();
            logTable.addMessage(lr);
        }
    });
}
}
