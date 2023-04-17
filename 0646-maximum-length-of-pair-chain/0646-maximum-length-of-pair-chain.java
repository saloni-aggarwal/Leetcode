class Solution {
    public int findLongestChain(int[][] pairs) {
        Arrays.sort(pairs, (a,b) -> a[0] - b[0]);
        // for(int[] pair: pairs) {
        //     System.out.print(Arrays.toString(pair) + " ");
        // }
        //  System.out.println();
        
        int[] dp = new int[pairs.length];
        Arrays.fill(dp, 1);
        
        for(int i = 1; i < pairs.length; i++) {
            // int last = pairs[i][1];
            for(int j = 0; j < i; j++) {
                if(pairs[j][1] < pairs[i][0]) {
                    dp[i] = Math.max(dp[i], dp[j]+1);                    
                }
            }
        }
        
        int ans = 0;
        for(int val: dp) {
            if(val > ans){
                ans = val;
            }
        }
        return ans;
    }
}