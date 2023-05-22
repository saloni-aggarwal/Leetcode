class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> cnt = new HashMap<>();
        
        for(int num: nums) {
            cnt.put(num, cnt.getOrDefault(num, 0)+1);
        }
        
        PriorityQueue<Integer> pq = new PriorityQueue<>((a,b) -> cnt.get(b)-cnt.get(a));
        
        for(int num: cnt.keySet()) {
            pq.add(num);
        }
        
        int[] ans = new int[k];
        
        for(int i = 0; i < k; i++) {
            ans[i] = pq.poll();
        }
        return ans;
    }
}
            
        