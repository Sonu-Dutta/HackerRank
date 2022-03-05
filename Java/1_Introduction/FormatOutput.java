import java.util.Scanner;
public class FormatOutput {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("================================");
        for(int i=0;i<3;i++){
            String s1=sc.next();
            int x=sc.nextInt();
            System.out.printf("%-15s%03d\n",s1,x); //-15 for left-justify and 03 for to occupy 3 places in digits
        }
        System.out.println("================================");
        sc.close();
}

}
