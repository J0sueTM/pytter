import java.awt.*;
import java.awt.event.*;
import java.awt.event.ActionListener;

import javax.swing.*;

public class Main {
    public static int count = 0;

    public static JFrame mainFrame;
    public static JPanel mainPanel;

    public static JButton mainButton;
    public static JLabel mainLabel;

    public Main() {
        mainFrame = new JFrame();
        mainPanel = new JPanel();

        mainButton = new JButton("Click me");
        mainLabel = new JLabel("Number of clicks: ");

        mainButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                ++count;

                mainLabel.setText(mainLabel.getText() + count);
            }
        });

        mainPanel.setBorder(BorderFactory.createEmptyBorder(30, 30, 10, 30));
        mainPanel.setLayout(new GridLayout(0, 1));
        mainPanel.add(mainButton);
        mainPanel.add(mainLabel);

        mainFrame.add(mainPanel, BorderLayout.CENTER);
        mainFrame.setTitle("Window");
        mainFrame.setSize(800, 600);
        mainFrame.setResizable(false);
        mainFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        mainFrame.pack();
        mainFrame.setVisible(true);
    }

    public static void main(String[] args) {
        new Main();
    }
}