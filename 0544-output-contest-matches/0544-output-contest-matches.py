class Solution:
    def findContestMatch(self, n: int) -> str:
        arr = []
        for i in range(1, n+1):
            arr.append(str(i))
        
        
        while n > 1:
            for i in range(0, n//2):
                arr[i] = "(" + arr[i] + "," + arr[n-i-1] + ")"
            print(arr)
            n //= 2
        return arr[0]
            
        