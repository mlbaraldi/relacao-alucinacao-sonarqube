package generated;
public class Generated96dfb201e672 {
public static void selectRow(int row,JTable table,JScrollPane pane){
    table.setRowSelectionInterval(row, row);
    table.changeSelection(row, 0, false, false);
    pane.getViewport().setViewPosition(new Point(0, table.getRowHeight() * row));
    pane.revalidate();
    pane.repaint();
}
}
