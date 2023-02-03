class SparseVector:
    def __init__(self, nums: List[int]):
        self.vector = nums
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        total = 0
        for i in range(len(vec.vector)):
            total += self.vector[i] * vec.vector[i]
        return total
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)