public class Solution {
    
     public static String solution(long x, long y) {
        long nextVal;
        long currVal = 1;
        
        // First, compute values in the first row until we reach our target column
        for(long i = 1; i < x; i++){
            nextVal = currVal + i + 1; //Plus 1 because we're staying on the first row
            currVal = nextVal;
        }
        
        // Second, compute values in the target column up until we reach our target row
        for(long i = 2; i <= y; i++){
        
            nextVal = currVal + x + i - 2;
            currVal = nextVal;
        }
        
        return ""+currVal;
        

    }
}
