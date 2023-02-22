class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        kArr = [int(s) for s in str(k)]
        i, j = len(num)-1, len(kArr)-1
        carry = 0
        while i >= 0 and j >= 0:
            s = num[i] + kArr[j] + carry
            num[i] = s % 10
            carry = s // 10
            i -= 1
            j -= 1
        while i >= 0:
            s = num[i] + carry 
            num[i] = s % 10
            carry = s // 10
            i -= 1
        while j >= 0:
            s = kArr[j] + carry 
            num.insert(0, s % 10)
            carry = s // 10
            j -= 1
        if carry > 0:
            num.insert(0, carry)
        return num
            
        