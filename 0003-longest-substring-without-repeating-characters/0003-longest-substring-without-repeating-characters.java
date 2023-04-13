class Solution {
    public int lengthOfLongestSubstring(String s) {
        List<Character> seq = new ArrayList<>();
        int len = 0;
        for(int i = 0; i < s.length(); i++) {
            if(seq.contains(s.charAt(i))) {
                len = Math.max(len, seq.size());
                int idx = seq.indexOf(s.charAt(i));
                seq = seq.subList(idx+1, seq.size());
            }
            seq.add(s.charAt(i));
            // System.out.println(seq);
        }
        return Math.max(len, seq.size());
    }
}