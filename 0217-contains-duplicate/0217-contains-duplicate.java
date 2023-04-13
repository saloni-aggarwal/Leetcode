class Solution {
    public boolean containsDuplicate(int[] nums) {
        Map<Integer, Integer> cnt = new HashMap<>();
        for(int num: nums) {
            int val = cnt.getOrDefault(num, 0)+1;
            if(val >= 2)
                return true;
            cnt.put(num, val);
        }
        return false;
        
    }
}