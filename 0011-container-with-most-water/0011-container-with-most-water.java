class Solution {
    public int maxArea(int[] height) {
        int biggestArea = 0;
        int left = 0, right = height.length-1;
        
        while(left < right) {
            int currentArea = Math.min(height[left], height[right]) * (right-left);
            biggestArea = Math.max(biggestArea, currentArea);
            
            if(height[left] <= height[right])
                left += 1;
            else
                right -= 1;
            
        }
        
        return biggestArea;        
    }
}