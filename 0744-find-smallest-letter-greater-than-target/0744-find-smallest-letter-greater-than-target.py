class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        i, j = 0, n-1
                
        while i <= j:
            mid = (i+j)//2
            
            if ord(letters[mid]) < ord(target):
                i = mid + 1
                
            elif ord(letters[mid]) > ord(target):
                j = mid - 1
                
            else:
                while mid < n and letters[mid] == target:
                    mid += 1
                    
                return letters[(mid)%n]
            
        return letters[i%n]
        