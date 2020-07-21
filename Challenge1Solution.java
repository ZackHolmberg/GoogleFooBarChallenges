public static String solution(String x) {
        
        String string;
        StringBuilder tempString = new StringBuilder();

        for(int i = 0; i < x.length(); i++)
        {
            char temp = x.charAt(i);
            int temp2 = (int) temp;
            if(temp2 > 122 || temp2 < 97){
                tempString.append(temp);
                System.out.println("Appended: "+temp);

            } else {
                char resultCharacter = (char) (122 - ((int) temp - 97));
                tempString.append(resultCharacter);
                System.out.println("Appended: "+resultCharacter);

            }
        }
        
        string = tempString.toString();
        System.out.println("Outputting: "+string);
        return string;
    }
