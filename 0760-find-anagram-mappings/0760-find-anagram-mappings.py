class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter = collections.Counter(nums2)
        index = collections.defaultdict(list)
        
        for i, num in enumerate(nums2):
            index[num].append(i)
            
        res = []
        
        for num in nums1:
            res.append(index[num][counter[num]-1])
            counter[num] -= 1
        return res
            