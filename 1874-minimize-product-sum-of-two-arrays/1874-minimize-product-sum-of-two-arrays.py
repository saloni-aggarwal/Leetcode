class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort(reverse=True)
        total = 0
        for lst in zip(nums1, nums2):
            total += (lst[0] * lst[1])
        return total
        