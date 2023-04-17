class Solution {
//     Method 1
//     public boolean isPalindrome(String s, int i, int j) {
//         while(i < j) {
//             if(s.charAt(i++) != s.charAt(j--))
//                 return false;
//         }
//         return true;
//     }
//     public int countSubstrings(String s) {
//         int ans = 0;
        
//         for(int i = 0; i < s.length(); i++) {
//             for(int j = i; j < s.length(); j++) {
//                 if(isPalindrome(s, i, j)) {
//                     ans += 1;
//                 }
//             }
//         }
//         return ans;
        
//     }
    int ans = 0;
    public void countSubStr(String s, int i, int j) {
        // int ans = 0;
        
        while(i >= 0 && j < s.length()) {
            if(s.charAt(i--) != s.charAt(j++))
                break;
            ans += 1;
        }
        // return ans;
    }
    
     public int countSubstrings(String s) {
         // int ans = 0;
         
         for(int i = 0; i < s.length(); i++) {
             countSubStr(s, i, i);
             countSubStr(s, i, i+1);
         }
         return ans;
     }
}