class Solution {
    public boolean checkInclusion(String s1, String s2) {
        
        char[] temp;
        
        temp = s1.toCharArray();
        Arrays.sort(temp);
        s1 = new String(temp);
        
        int len = s1.length();
        
        for(int i = 0; i <= s2.length()-len; i++) {
            temp = s2.substring(i, i+s1.length()).toCharArray();
            Arrays.sort(temp);
            String compare = new String(temp);
            
            if(compare.equals(s1)) {
                return true;
            }
        }
        
        return false;
    }
}