public class Solution {
    public static int solution(String s) {
        
        // Determine how many interactions will occur and times that number by 2 to compute the number of salutes.
        // To determine the number of interactions, simply check how many < are to the right of every >
        int interactions = 0;
        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) == '>'){
                for(int j = i; j < s.length(); j++){
                    if(s.charAt(j) == '<'){
                        interactions++;
                    }
                }
            }    
        }
        
        return interactions * 2;
    }
}
