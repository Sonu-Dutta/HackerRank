public class Practice {
   
      public static void main(String[] args) {
        String b="unos";
        String ch="sonu";
    
        if (b.indexOf(ch) != -1) {
            b = b.replaceFirst(ch + "", "");
            System.out.println(b);
          } 
          else {
            System.out.println("false");
          }
      }
}
