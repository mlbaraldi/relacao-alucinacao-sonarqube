package generated;
public class Generatede68949d37df1 {
public void addMessage(final LogRecord lr){
    SwingUtilities.invokeLater(new Runnable() {
        @Override
        public void run() {
            // Assuming the LogTable's model is accessible and has an addLogRecord method
            // Replace with actual code to add the log record to the model
            DefaultTableModel model = (DefaultTableModel) logTable.getModel();
            Vector<Object> rowData = new Vector<>();
            rowData.add(lr.getLevel());
            rowData.add(lr.getMessage());
            rowData.add(new Date(lr.getMillis()));
            model.addRow(rowData);
        }
    });
}
}
