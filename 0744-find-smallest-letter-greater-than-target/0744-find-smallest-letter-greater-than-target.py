class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # print("STARTING NEW")
        i, j = 0, len(letters)-1
                
        while i <= j:
            # print("i =", i, " j =", j)
            mid = (i+j)//2
            # print("mid =", mid)
            if ord(letters[mid]) < ord(target):
                # print("in if")
                i = mid + 1
            elif ord(letters[mid]) > ord(target):
                # print("in elif")
                j = mid - 1
            else:
                while mid < len(letters) and letters[mid] == target:
                    mid += 1
                return letters[(mid)%len(letters)]
        # print("i =", i, " j =", j)
            
        return letters[i%len(letters)]
        