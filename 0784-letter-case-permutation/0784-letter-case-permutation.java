class Solution {
    
    List<String> ans = new ArrayList<>();
    
    public void recurs(String s, int idx, int n) {
        if(idx == n) {
            if(!ans.contains(s)) {
                ans.add(s);
            }
            return;
        }
        
        if(Character.isLetter(s.charAt(idx))){
            recurs(s.substring(0, idx)+Character.toLowerCase(s.charAt(idx))+s.substring(idx+1, n), idx+1, n);
            recurs(s.substring(0, idx)+Character.toUpperCase(s.charAt(idx))+s.substring(idx+1, n), idx+1, n);
        } else {
            recurs(s, idx+1, n);
        }
        
    }
    public List<String> letterCasePermutation(String s) {
        recurs(s, 0, s.length());
        return ans;
    }
}