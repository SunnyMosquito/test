import java.awt.AWTException;
import java.awt.Image;
import java.awt.MenuItem;
import java.awt.PopupMenu;
import java.awt.SystemTray;
import java.awt.Toolkit;
import java.awt.TrayIcon;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Test {

private static final String TOOLTIP = "tray test";
private static final String IMAGE = "/usr/share/pixmaps/gnome-gmush.png";
private static PopupMenu menu;

public static void main(String[] args) {
new Test().start();
}

private void start() {
if (SystemTray.isSupported()) {
SystemTray tray = SystemTray.getSystemTray();
Image trayImage = Toolkit.getDefaultToolkit().getImage(IMAGE);
createMenu();
TrayIcon trayIcon = new TrayIcon(trayImage, TOOLTIP, menu);
trayIcon.setImageAutoSize(true);
try {
tray.add(trayIcon);
trayIcon.displayMessage("caption", "howdy", TrayIcon.MessageType.INFO);
} catch (AWTException e) {
System.err.println("Error starting tray: " + e);
}

} else {
System.err.println("SystemTray not supported");
}
}

private void createMenu() {
menu = new PopupMenu();
MenuItem foo = new MenuItem("foo");
MenuItem exit = new MenuItem("exit");
exit.addActionListener(new exitListener());
menu.add(foo);
menu.addSeparator();
menu.add(exit);
}

class exitListener implements ActionListener {

public void actionPerformed(ActionEvent e) {
System.out.println("exiting...");
System.exit(0);
}
}
}