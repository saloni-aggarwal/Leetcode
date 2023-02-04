class Solution {
    public int[] minOperations(String boxes) {
        int length = boxes.length();
        int[] res = new int[length];
        int[] right = new int[length];
        int cnt = 0, ops = 0;
        for(int i = 0; i < length; i++) {
            res[i] += ops;
            cnt += boxes.charAt(i) == '1' ? 1 : 0;
            ops += cnt;
        }
        ops = 0; 
        cnt = 0;
        for(int i = length-1; i >= 0; i--) {
            res[i] += ops;
            cnt += boxes.charAt(i) == '1' ? 1 : 0;
            ops += cnt;
        }
        // System.out.println(Arrays.toString(res));
        return res;
    }
}