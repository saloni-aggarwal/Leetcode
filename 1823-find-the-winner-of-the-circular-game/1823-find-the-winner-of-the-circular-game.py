class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i for i in range(1, n+1)]

        
        def recurse(arr, i, n, k):
            if len(arr) == 1:
                return arr[0]
            i = ((i+k)%n)-1
            arr.pop(i)
            if i == -1:
                i = 0
            return recurse(arr, i, n-1, k)

        return recurse(arr, 0, n, k)
        