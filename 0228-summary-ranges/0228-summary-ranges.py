class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        start = i = nums[0]
        # st = ""
        ans = []
        for j in range(len(nums)):
            # print("i =", i, "j =", j, "nums[j] =", nums[j])
            # print("start =", start)
            if i != nums[j]:
                # print("in if")
                if start != nums[j-1]:
                    st = str(start) + "->" + str(nums[j-1])
                else:
                    st = str(start)
                ans.append(st)
                if j != len(nums):
                    start = i = nums[j]
            # else:
                # print("in else")
            i += 1
        if start != nums[-1]:
            st = str(start) + "->" + str(nums[-1])
        else:
            st = str(start)
        ans.append(st)
        return ans
            