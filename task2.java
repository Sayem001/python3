public class Task2 {
    public static void main(String[] args) {
        String id1 = "TIKA-2104";
        double files = 8.0;
        String id2 = "TIKA-317";
        double dmm = 0.45;

        int n = Integer.parseInt(id1.split("-")[1]) 
              + Integer.parseInt(id2.split("-")[1]);

        int digits = 0;
        while (n > 0) {
            n = n / 10;
            digits++;
        }

        int impact = (int) (files * dmm);

        System.out.println("Combined digits: " + digits);
        System.out.println("Impact: " + impact);
    }
}