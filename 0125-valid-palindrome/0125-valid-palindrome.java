class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder st = new StringBuilder();
        for(int i = 0; i < s.length(); i++) {
            if(Character.isAlphabetic(s.charAt(i)) || Character.isDigit(s.charAt(i))) {
                st.append(Character.toLowerCase(s.charAt(i)));
            }
        }
        int i = 0, j = st.length()-1;
        while(i < j) {
            if(st.charAt(i) != st.charAt(j))
                return false;
            i += 1;
            j -= 1;
        }
        return true;
    }
}