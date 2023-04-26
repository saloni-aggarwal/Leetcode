class Solution {
    public int minMeetingRooms(int[][] intervals) {
        if (intervals.length == 0)
            return 0;
        
        Arrays.sort(intervals, new Comparator<>() {
            public int compare(int[] a, int[] b) {
                return Integer.compare(a[0], b[0]);
            }
        });
        
        PriorityQueue<Integer> track = new PriorityQueue<>();
        track.add(intervals[0][1]);
        
        for(int i = 1; i < intervals.length; i++) {
            if(track.peek() <= intervals[i][0])
                track.poll();
            track.add(intervals[i][1]);            
        }
        
        return track.size();
    }
}