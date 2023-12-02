import java.util.*;

public class Aggressive_cows {

    private static boolean isValid(int mid, int[] A, int c){
      int count = 1;
      int prev = A[0];

      for(int i = 1; i < A.length; i++){
        if(A[i] - prev >= mid) {
          count++;
          prev = A[i];
        }
        if (count >= c) {
          return true;
        }
      }

      return false;
    }

    public static void main(String[] args) {
      
      Scanner sc = new Scanner(System.in);
      int t = sc.nextInt();

      while(t > 0) {
        int n = sc.nextInt();
        int c = sc.nextInt();

        int[] A = new int[n];

        for(int i = 0; i < n; i++){
          A[i] = sc.nextInt();
        }

        Arrays.sort(A);

        int high = 1000000001;
        int low = 0;
        int ans = 0;

        while(low <= high){
          int mid = low + (high - low) / 2;

          if(isValid(mid, A, c)){
            ans = mid;
            low = mid + 1;
          }
          else {
            high = mid - 1;
          }
        }

        System.out.println(ans);
        t--;
      }
  }
}