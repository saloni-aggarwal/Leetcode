class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Method 1
        
/*         Map<Integer, List<Integer>> idx = new HashMap<>();
        Map<Integer, Integer> count = new HashMap<>();
        List<Integer> temp;
        for(int i = 0; i < nums.length; i++) {
            temp = idx.getOrDefault(nums[i], new ArrayList<>());
            temp.add(i);
            idx.put(nums[i], temp);
            count.put(nums[i], count.getOrDefault(nums[i], 0)+1);
        }
        
        for(int num: nums) {
            int remaining = target - num;
            if(remaining == num && count.get(num) > 1) {
                return new int[]{idx.get(num).get(0), idx.get(num).get(1)};
            } else if(remaining != num && idx.containsKey(remaining)) {
                return new int[]{idx.get(num).get(0), idx.get(remaining).get(0)};
            }
        } */
        
        Map<Integer, Integer> idx = new HashMap<>();
        for(int i = 0; i < nums.length; i++) {
            if(idx.containsKey(nums[i])) {
                int val = idx.get(nums[i]);
                return new int[]{val, i};
            } else {
                idx.put(target-nums[i], i);
            }
        }
        
        return new int[2];
    }
}