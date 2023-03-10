class Solution:
    def digitCount(self, num: str) -> bool:
        numCnt = Counter(num)
        print(numCnt)
        # n = len(num)
        # for i in range(len(num)):
        #     numCnt[i] = 0
        #     numCnt[num[i]] += 1
        for i in range(len(num)):
            print("i =", i)
            print(numCnt[i])
            print("num[i] =", num[i])
            if numCnt[str(i)] != int(num[i]):
                return False
        return True
                
            
            
        
        