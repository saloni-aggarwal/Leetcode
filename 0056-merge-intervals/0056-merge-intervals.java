class Solution {
    public int[][] merge(int[][] intervals) {
        
        int[][] res = new int[intervals.length][2];
        int idx = 0, idx2 = 0;
        
        Arrays.sort(intervals, Comparator.comparingInt(o -> o[0]));
        
        while(idx < intervals.length) {
            int start = intervals[idx][0];
            int end = intervals[idx][1];
            while(idx < intervals.length && intervals[idx][0] <= end) {
                end = Math.max(end, intervals[idx++][1]);
            }
            res[idx2++] = new int[]{start, end};
        }
        
        return Arrays.copyOfRange(res, 0, idx2);
        
    }
}