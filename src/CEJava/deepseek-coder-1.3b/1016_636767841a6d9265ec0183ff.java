package generated;
public class Generated96dfb201e672 {
public static void selectRow(int row,JTable table,JScrollPane pane){
    // Get the selected model
    DefaultTableModel model = (DefaultTableModel) table.getModel();

    // Set the selection model
    table.setSelectionModel(new DefaultTableSelectionModel(model) {
        @Override
        public void setSelectionInterval(RowSelectionInterval interval) {
            super.setSelectionInterval(interval);
            // Scroll to the selected row
            if (interval != null) {
                pane.setViewportView(table).scrollRectToVisible(new Rectangle(interval.getFirstRow(), 0, 1, 1));
            }
        }
    });

    // Select the row
    table.setRowSelectionInterval(row, row);

    // Repaint the table
    table.repaint();
}
}
