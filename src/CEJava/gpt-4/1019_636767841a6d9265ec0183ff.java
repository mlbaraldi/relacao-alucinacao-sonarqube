package generated;
public class Generated96dfb201e672 {
public static void selectRow(int row,JTable table,JScrollPane pane){
    if (row >= 0 && row < table.getRowCount()) {
        // Select the specified row
        table.setRowSelectionInterval(row, row);

        // Scroll the table to make the selected row visible
        Rectangle rect = table.getCellRect(row, 0, true);
        table.scrollRectToVisible(rect);

        // Repaint the table after a delay to ensure the selected row is properly painted
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                table.repaint();
            }
        });
    } else {
        System.out.println("Row out of range");
    }
}
}
