class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        Set<Integer> set1 = new HashSet<>();
        for(int num: nums1){
            set1.add(num);
        }
        
        Set<Integer> set2 = new HashSet<>();
        for(int num: nums2){
            set2.add(num);
        }
        
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> temp = new ArrayList<>();
        
        for(int num: set1) {
            if(!set2.contains(num))
                temp.add(num);
        }
        
        res.add(temp);
        temp = new ArrayList<>();
        
        for(int num: set2) {
            if(!set1.contains(num))
                temp.add(num);
        }
        res.add(temp);
        
        return res;
    }
}