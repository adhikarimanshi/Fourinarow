import javax.swing.*;    // Importing Swing components like JFrame, JButton, JTextField
import java.awt.*;       // Importing AWT classes, including FlowLayout
import java.awt.event.*; // Importing AWT event-handling classes

public class HelloWorldGUI {
    public static void main(String[] args) {
        // Create a JFrame (window)
        JFrame frame = new JFrame("Hello World GUI");

        // Create a text field
        JTextField textField = new JTextField(20);
        textField.setEditable(false); // Make text field non-editable

        // Create a button
        JButton button = new JButton("Click Me");

        // Add action listener to the button
        button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // When button is clicked, set text field to "Hello World"
                textField.setText("Hello World");
            }
        });

        // Add components to the frame
        frame.setLayout(new FlowLayout());
        frame.add(textField);
        frame.add(button);

        // Set frame properties
        frame.setSize(300, 100);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}
