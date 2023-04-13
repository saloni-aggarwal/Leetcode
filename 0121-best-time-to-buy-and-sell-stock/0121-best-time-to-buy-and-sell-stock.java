class Solution {
    public int maxProfit(int[] prices) {
        int[] maxTrack = new int[prices.length];
        maxTrack[prices.length-1] = prices[prices.length-1];
        for(int i = prices.length-2; i >= 0; i--) {
            maxTrack[i] = Math.max(maxTrack[i+1], prices[i]);
        }
        int ans = 0;
        for(int i = 0; i < prices.length; i++) {
            ans = Math.max(ans, maxTrack[i]-prices[i]);
        }
        return ans;
    }
}