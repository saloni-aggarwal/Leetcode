class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        
        res = []
        i, j, k = 0, 0, 0
        
        while i < len(arr1) and j < len(arr2) and k < len(arr3):
            ele = arr1[i]
            
            while j < len(arr2) and arr2[j] < ele:
                j += 1
                
            while k < len(arr3) and arr3[k] < ele:
                k += 1
                
            if j < len(arr2) and arr2[j] == ele and k < len(arr3) and arr3[k] == ele:
                res.append(ele)
            i += 1
            
        return res
            
        
        
        