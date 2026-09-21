package generated;
public class Generated96dfb201e672 {
public static void selectRow(int row,JTable table,JScrollPane pane){
    // Select the specified row in the table
    table.setRowSelectionInterval(row, row);
    
    // Calculate the rectangle of the row to scroll to
    Rectangle rect = table.getCellRect(row, 0, true);
    table.scrollRectToVisible(rect);
    
    // Schedule a repaint after the current events are processed to ensure proper rendering
    SwingUtilities.invokeLater(() -> {
        table.repaint();
        pane.repaint();
    });
}
}
