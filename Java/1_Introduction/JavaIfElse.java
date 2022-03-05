import java.util.Scanner;
public class JavaIfElse{
    public static void main(String[] args) {
        
        Scanner s = new Scanner(System.in);
        System.out.print("Enter number:");        
        int N=s.nextInt();
        if(N%2!=0){
            System.out.println("Weird");
        }
        else if(N%2==0 & N>=2 & N<=5){
            System.out.println("Not Weird");
        }
        else if(N%2==0 & N>=6 & N<=20){
            System.out.println("Weird");
        }
        else {
            System.out.println("Not Weird");
        }
     s.close();
    }
    
}