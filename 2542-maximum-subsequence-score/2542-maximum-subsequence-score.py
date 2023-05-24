class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        sorted_pairs = sorted(zip(nums1, nums2), key= lambda x: -x[1])
        # print("sorted_pairs =", sorted_pairs)
        
        ans, total = 0, 0
        heap = []
        
        for pair in sorted_pairs:
            num1, num2 = pair  
            heappush(heap, num1)
            
            total += num1
            if len(heap) > k:
                total -= heappop(heap)
            if len(heap) == k:
                ans = max(ans, total * num2)
            # print("heap = ", heap)
            # print("ans = ", ans)
        
        return ans