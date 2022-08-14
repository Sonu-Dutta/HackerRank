import java.util.*;
import java.util.Scanner;
public class JavaArrayList {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        ArrayList[] arrayLists=new ArrayList[20000];
        for(int i=0;i<n;i++){
            arrayLists[i]= new ArrayList<>();
            int d=sc.nextInt();
            for(int j=0;j<d;j++){
                int value=sc.nextInt();
                arrayLists[i].add(value);
            }
        }
        int q=sc.nextInt();
        for(int i=0;i<q;i++){
            int row=sc.nextInt();
            int column=sc.nextInt();
            try{
            System.out.println(arrayLists[row-1].get(column-1));
            }
            catch(Exception e){
                System.out.println("ERROR!");
            }
        }
       
        sc.close();
    }
}