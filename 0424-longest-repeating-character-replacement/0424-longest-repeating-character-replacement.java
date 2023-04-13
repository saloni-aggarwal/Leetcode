class Solution {
    public int characterReplacement(String s, int k) {
        int[] arr = new int[26];
        int beg = 0, maxLen = 0, largestCnt = 0;
        
        for(int end = 0; end < s.length(); end++) {
            arr[s.charAt(end) - 'A']++;
            largestCnt = Math.max(largestCnt, arr[s.charAt(end) - 'A']);
            
            if(end - beg + 1 - largestCnt > k) {
                arr[s.charAt(beg++) - 'A'] --; 
                System.out.println(Arrays.toString(arr));
            }
            
            maxLen = Math.max(maxLen, end-beg+1);
        }
        return maxLen;
        
    }
}