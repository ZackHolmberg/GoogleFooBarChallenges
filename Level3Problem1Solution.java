import java.util.ArrayList;

class Solution {  
    
    public static int solution(int start, int length) {
        
        if(length == 1){
            return 0 ^ start;
        }

        int toIgnore = 0;
        int toReturn = 0;
        int toRead = length;
        int val = start;
        int tempVal = 0;            
        
        while(toRead != 0){
            toRead = length - toIgnore;
            for(int i = 0; i < toRead; i++){
                tempVal = val + i;
                toReturn = toReturn ^ tempVal;

            }
            val = tempVal + toIgnore + 1;
            toIgnore++;
        }
        
        return toReturn;
        
    }
}
