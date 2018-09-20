import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.net.URL;

public class Calculator {
    private String str1 = "0";
    private String str2 = "0";
    private String signal = "+";
    private String result = "0";
    // 开关1用于选择输入方向，将要写入str1或str2
    int k1 = 1;
    // 开关2用于记录符号键的次数，如果 k2>1 说明进行的是 2+3-9+8 这样的多符号运算
    int k2 = 1;
    // 开关3用于标识 str1 是否可以被清0 ，等于1时可以，不等于1时不能被清0
    int k3 = 1;
    // 开关4用于标识 str2 是否可以被清0
    int k4 = 1;
    // 开关5用于控制小数点可否被录入，等于1时可以，不为1时，输入的小数点被丢掉
    int k5 = 1;
    // store的作用类似于寄存器，用于记录是否连续按下符号键
    JButton store;
    JFrame frame = new JFrame("Calculator");
    JTextField result_TextField = new JTextField(result, 20);
    JButton clear_Button = new JButton("Clear");
    JButton button0 = new JButton("0");
    JButton button1 = new JButton("1");
    JButton button2 = new JButton("2");
    JButton button3 = new JButton("3");
    JButton button4 = new JButton("4");
    JButton button5 = new JButton("5");
    JButton button6 = new JButton("6");
    JButton button7 = new JButton("7");
    JButton button8 = new JButton("8");
    JButton button9 = new JButton("9");
    JButton button_Dian = new JButton(".");
    JButton button_jia = new JButton("+");
    JButton button_jian = new JButton("-");
    JButton button_cheng = new JButton("*");
    JButton button_chu = new JButton("/");
    JButton button_dy = new JButton("=");

    public Calculator() {
	
	    // 为按钮设置等效键，即可以通过对应的键盘按键来代替点击它
		button0.setMnemonic(KeyEvent.VK_0);
		// 其它等效键省略，你可以自行补充完整
        // 设置文本框为右对齐，使输入和结果都靠右显示
		result_TextField.setHorizontalAlignment(JTextField.RIGHT);
        // 将UI组件添加进容器内
		JPanel pan = new JPanel();
		pan.setLayout(new GridLayout(4, 4, 5, 5));
		pan.add(button7);
		pan.add(button8);
		pan.add(button9);
		pan.add(button_chu);
		pan.add(button4);
		pan.add(button5);
		pan.add(button6);
		pan.add(button_cheng);
		pan.add(button1);
		pan.add(button2);
		pan.add(button3);
		pan.add(button_jian);
		pan.add(button0);
		pan.add(button_Dian);
		pan.add(button_dy);
		pan.add(button_jia);
		pan.setBorder(BorderFactory.createEmptyBorder(5, 5, 5, 5));

		JPanel pan2 = new JPanel();
		pan2.setLayout(new BorderLayout());
		pan2.add(result_TextField, BorderLayout.WEST);
		pan2.add(clear_Button, BorderLayout.EAST);

        // 设置主窗口出现在屏幕上的位置
		frame.setLocation(300, 200);
		// 设置窗体不能调大小
		frame.setResizable(false); 
		frame.getContentPane().setLayout(new BorderLayout());
		frame.getContentPane().add(pan2, BorderLayout.NORTH);
		frame.getContentPane().add(pan, BorderLayout.CENTER);

        frame.pack();
        frame.setVisible(true);

        // 数字键
        class Listener implements ActionListener {
            public void actionPerformed(ActionEvent e) {
				String ss = ((JButton) e.getSource()).getText();
                store = (JButton) e.getSource();
                result_TextField.setText(ss + store);
            }
        }

        // 监听数字键
        Listener jt = new Listener();

        button7.addActionListener(jt);
        button8.addActionListener(jt);
        button9.addActionListener(jt);
        button4.addActionListener(jt);
        button5.addActionListener(jt);
        button6.addActionListener(jt);
        button1.addActionListener(jt);
        button2.addActionListener(jt);
        button3.addActionListener(jt);
        button0.addActionListener(jt);

        // 窗体关闭事件的响应程序
        frame.addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent e) {
                if (SystemTray.isSupported()) {
                    URL resource = this.getClass().getResource("/img.jpg");
                    ImageIcon icon = new ImageIcon(resource);
                    PopupMenu popupMenu = new PopupMenu();
                    MenuItem item = new MenuItem("退出");
                    item.addActionListener(new ActionListener(){
                        @Override
                        public void actionPerformed(ActionEvent e) {
                            System.exit(0);                            
                        }
                    });
                    popupMenu.add(item);
                    TrayIcon trayIcon = new TrayIcon(icon.getImage(),"使用系统托盘",popupMenu);
                    SystemTray systemTray = SystemTray.getSystemTray();
                    try {
                        systemTray.add(trayIcon);                        
                    } catch (Exception ee) {
                        ee.printStackTrace();
                    }
                } else {
                    System.exit(0);
                }
            }
        });
    }

    public static void main(String[] args) {
        // 设置程序显示的界面风格，可以去除
	    try {
			UIManager.setLookAndFeel("javax.swing.plaf.metal.MetalLookAndFeel");
		} catch (Exception e) {
			e.printStackTrace();
		}
		Calculator cal = new Calculator();
    }
}