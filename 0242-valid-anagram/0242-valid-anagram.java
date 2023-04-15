class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> sCnt = new HashMap<>();
        HashMap<Character, Integer> tCnt = new HashMap<>();
        
        if(s.length() != t.length())
            return false;
        
        for(int i = 0; i < s.length(); i++) {
            sCnt.put(s.charAt(i), sCnt.getOrDefault(s.charAt(i), 0) + 1);
        }
        for(int i = 0; i < t.length(); i++) {
            tCnt.put(t.charAt(i), tCnt.getOrDefault(t.charAt(i), 0) + 1);
        }
        
        for(Character key: sCnt.keySet()) {
            int val1 = tCnt.getOrDefault(key, 0);
            int val2 = sCnt.get(key);
            if(val1 != val2)
                return false;
        }
        return true;
        
    }
}