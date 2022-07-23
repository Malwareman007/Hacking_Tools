// Package name here 

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.math.BigInteger;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
// Imported all needed libraries

public class SHA_256 {
	// This is Main class 
	JFrame frame;
	JLabel label, label_Data, label_Hash;
	JTextField text_Data,text_Hash;
	JButton get_button, reset_Button, quit_Button;
	Icon cross_icon;
	// Declaration of all Swing variables
	
    SHA_256(){
    	// Begining of Constructor
        frame=new JFrame("SHA_256");
        frame.setLayout(null);
        frame.setSize(500,370);
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // Frame Properites are set with no layout
        
        label=new JLabel("Hash Genrator");
        label.setFont(new Font("Serif", Font.BOLD, 26));
        label.setBounds(180,10,200,40);
        // Label Properites for top label
        
        label_Data = new JLabel("Enter data:");
        label_Data.setFont(new Font("Monospace", Font.BOLD,15));
        label_Data.setBounds(70,70,90,40);
        text_Data=new JTextField("");
        text_Data.setBounds(170, 77,210,30);
        // Label for data and field for input created
        
        label_Hash = new JLabel("Hash: ");
        label_Hash.setFont(new Font("Monospace", Font.BOLD,15));
        label_Hash.setBounds(70,120,80,40);
        text_Hash= new JTextField();
        text_Hash.setBounds(30, 180, 430, 50);
        text_Hash.setAlignmentX(FlowLayout.CENTER);
        // Label for Hash Text and output field created 
        
        get_button=new JButton("GET HASH");
        get_button.setBounds(170, 126, 130, 30);
        get_button.setFont(new Font("Times_New_Roman",Font.BOLD,15));
        // Button for executing encryption
        
        
        reset_Button=new JButton("Reset");
        reset_Button.setBounds(100, 250, 100, 40);
        reset_Button.setFont(new Font("Times_New_Roman", Font.BOLD, 15));
        // Button for reset both TextFields ie. text_Data and text_Hash
        
        cross_icon= new ImageIcon("C:\\Users\\ankit\eclipse-workspace\\programs\\src\\package\\quit_image.png");
        quit_Button=new JButton(cross_icon);
        quit_Button.setBounds(300, 250, 100, 40);
        quit_Button.setFont(new Font("Times_New_Roman", Font.BOLD, 15));
        // Button for quiting the program with image icon
        
        
        frame.setIconImage(new ImageIcon("C:\\Users\\ankit\\eclipse-workspace\\programs\\src\\package\\lock_png_1.png").getImage());
        // Setting icon or favicon in JFrame
        
        get_button.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
            	
                	String str2=text_Data.getText();
                	if(str2.length()>1) {
                	try {
						text_Hash.setText(toHex(getSHA(str2)));
					} catch (NoSuchAlgorithmException e1) {
						e1.printStackTrace();
					}
                	}
                	else {
                		JOptionPane.showMessageDialog(null,"Give some INPUT!!","Input Error", JOptionPane.WARNING_MESSAGE, null);
                	}
                }
        });
        // Get_Hash button's ActionListner calls encryption method for Hashing and shows output in text_Hash
        
        reset_Button.addActionListener(new ActionListener() {
        	public void actionPerformed(ActionEvent e) {
        		text_Data.setText("");
        		text_Hash.setText("");
        	}
        });
        // reset_Button's ActionListner clears all the text in text_Data and text_Hash
        
        
        quit_Button.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
            	System.exit(0);
            }});
        // quit_Button will quit the program by returning 0 ie. normal termination of program.
        
        frame.add(label_Data);
        frame.add(label_Hash);
        frame.add(text_Data);
        frame.add(text_Hash);
        frame.add(label);
        frame.add(get_button);
        frame.add(reset_Button);
        frame.add(quit_Button);
        frame.getContentPane();
        frame.setResizable(false);
        frame.setLocationRelativeTo(null);
       // Adding all the elements to frame
    }
    // End of Constructor
    
    public static byte[] getSHA(String input) throws NoSuchAlgorithmException {
    	MessageDigest md= MessageDigest.getInstance("SHA-256");
    	//takes arbitrary-sized data and output a fixed-length hash value
    	return md.digest(input.getBytes(StandardCharsets.UTF_8));
    }
    //Method returns hash values or message digest
    
    public static String toHex(byte[] Hash) {
    	BigInteger n=new BigInteger(1,Hash);
    	StringBuilder hex=new StringBuilder(n.toString(16));
    	// Convert message digest into hexadecimal value
    	
    	while(hex.length()<64) {
    		hex.insert(0, '0');
    	}
    	
    	return hex.toString();
    }
    // Returns string with hash code 
    
    
    public static void main(String[] args) throws Exception{
        SHA_256 Object= new SHA_256();
        Object.getClass();
    }
    //End of Main 
}
