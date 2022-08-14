import java.util.Scanner;
public class Loops2 {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.print("Enter number:");    
        int t=s.nextInt();    
        for(int i=0;i<t;i++){
            int a = s.nextInt();
            int b = s.nextInt();
            int n = s.nextInt();
            
            for(int j=0;j<n;j++){
                a=a+b;
                System.out.print(a+ " ");
                b=b*2;
            }
            System.out.println("");
        }
        s.close();
    }
}
