class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        ans = []
        for i in range(len(l)):
            subArr = nums[l[i]:r[i]+1]
            subArr.sort()
            flag = True
            # print("subArr =", subArr)
            for j in range(1, len(subArr)-1):
                if subArr[j-1] - subArr[j] != subArr[j] - subArr[j+1]:
                    flag = False
            ans.append(flag)
            # print("ans =", ans)
        return ans