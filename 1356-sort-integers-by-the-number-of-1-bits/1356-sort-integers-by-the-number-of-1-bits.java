class Solution {
    public int[] sortByBits(int[] arr) {
        Map<Integer, List<Integer>> cntList = new HashMap<>();
        List<Integer> temp;
        
        for(int val: arr) {
            int cnt = Integer.bitCount(val);
            temp = cntList.getOrDefault(cnt, new ArrayList<>());
            temp.add(val);
            cntList.put(cnt, temp);
        }
        
        int[] ans = new int[arr.length];
        int idx = 0;
        for(Map.Entry<Integer, List<Integer>> pair : cntList.entrySet()) {
            temp = pair.getValue();
            Collections.sort(temp);
            for(int val: temp) {
                ans[idx] = val;
                idx += 1;
            }
                
        }
        return ans;
    }
}