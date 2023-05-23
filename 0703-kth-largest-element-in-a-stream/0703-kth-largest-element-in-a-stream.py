class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = nums
        self.nums.sort(reverse=True)
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.nums) == 0 or self.nums[0] < val:
            self.nums.insert(0, val)
        elif self.nums[-1] > val:
            self.nums.insert(len(self.nums), val)
        else:
            for i in range(len(self.nums)):
                if self.nums[i] <= val:
                    self.nums.insert(i, val)
                    break
        # print(val)
        # print(self.nums)
        return self.nums[self.k-1]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)