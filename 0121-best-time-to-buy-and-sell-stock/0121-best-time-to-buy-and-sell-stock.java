class Solution {
    public int maxProfit(int[] prices) {
//         Approach 1
        /* int[] maxTrack = new int[prices.length];
        maxTrack[prices.length-1] = prices[prices.length-1];
        for(int i = prices.length-2; i >= 0; i--) {
            maxTrack[i] = Math.max(maxTrack[i+1], prices[i]);
        }
        int ans = 0;
        for(int i = 0; i < prices.length; i++) {
            ans = Math.max(ans, maxTrack[i]-prices[i]);
        }
        return ans; */
        
//         Approach 2
        int leftVal = Integer.MAX_VALUE;
        int profit = 0;
        for(int price: prices) {
            leftVal = Math.min(leftVal, price);
            profit = Math.max(profit, price-leftVal);
        }
        return profit;
    }
}