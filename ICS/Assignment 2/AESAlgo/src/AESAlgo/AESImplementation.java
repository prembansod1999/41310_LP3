package AESAlgo;

import java.util.Scanner;

public class AESImplementation {

	String convertStringToHexString(String str)
	{
	      StringBuffer sb = new StringBuffer();
	      //Converting string to character array
	      char ch[] = str.toCharArray();
	      for(int i = 0; i < ch.length; i++) {
	         String hexString = Integer.toHexString(ch[i]);
	         sb.append(hexString);
	      }
	      return sb.toString();
	}
	String convertHexStringToString(String str)
	{
		
	      String result = new String();
	      char[] charArray = str.toCharArray();
	      for(int i = 0; i < charArray.length; i=i+2) {
	         String st = ""+charArray[i]+""+charArray[i+1];
	         char ch = (char)Integer.parseInt(st, 16);
	         result = result + ch;
	      }
	      return result;
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);  // Create a Scanner object
		System.out.println("Enter text");
		
		String text = sc.nextLine();  
		AESImplementation obj = new AESImplementation();
		String hexText = obj.convertStringToHexString(text);
		System.out.println("Enter key");

		String key = sc.nextLine();  
		String hexKey = obj.convertStringToHexString(text);
		System.out.println("Input Text : " + text +"\nKey : "+key);
		AES aes= new AES(hexText,hexKey);
		System.out.println("Cipher Text : "+obj.convertHexStringToString(aes.encrypt()));
		System.out.println("Decrypted Text : "+obj.convertHexStringToString(aes.decrypt()));
		
	}

}
