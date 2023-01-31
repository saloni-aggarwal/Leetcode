class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def invert(S):
            num = {'0':'1', '1':'0'}
            return ''.join(num[i] for i in S)
        
        def reverse(st):
            return ''.join(s for s in reversed(st))
        
        arr = []
        for i in range(1, n+1):
            if i == 1:
                arr.append("0")
            else:
                st = arr[i-2] + "1" + reverse(invert(arr[i-2]))
                arr.append(st)
        return arr[-1][k-1]
        