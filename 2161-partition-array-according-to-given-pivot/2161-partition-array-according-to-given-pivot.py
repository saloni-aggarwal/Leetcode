class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        lessThan = []
        moreThan = []
        sameCnt = 0
        for num in nums:
            if num < pivot:
                lessThan.append(num)
            elif num > pivot:
                moreThan.append(num)
            else:
                sameCnt += 1
        return lessThan + [pivot] * sameCnt + moreThan