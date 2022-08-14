import java.util.*;

public class Array_1D {

    public static void main(String[] args) {
	   
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int[] a = new int[n];
        for(int i = 0 ; i < n; i++){
            int val = scan.nextInt();
            a[i]=val;
        }
        scan.close();
        for(int i = 0 ; i < n; i++){
            System.out.println(a[i]);
        }
    }
}