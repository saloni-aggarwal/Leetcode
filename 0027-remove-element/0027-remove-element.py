class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # print("NUMS =", nums)
        i, j = 0, len(nums)-1
        
        while i < j:
            # print("i and j before =", i, j)
            nums[i], nums[j] = nums[j], nums[i]
            while j > i and nums[j] == val:
                j -= 1
                
            while i <= j and nums[i] != val:
                i += 1
                
            # print("i and j after =", i, j)
#             
            # i += 1
            # j -= 1
        #     print("nums =", nums)
        # print("i outside =", i)
        # print("j outside =", j)
        if i == j:
            if nums[j] != val:
                # i += 1
                # nums[i] = nums[j-1]
                i += 1
            
            
        return i
        