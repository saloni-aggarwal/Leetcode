class Solution:
    
    def check(self, word):
        chFreq = Counter(word)
        uniqueFreq = set(chFreq.values())
        if len(uniqueFreq) == 1:
            return True
        return False
            
    def equalFrequency(self, word: str) -> bool:
#         chFreq = Counter(word)
        
# #         If there are only one kind of characters in word 
# #         eg: "zzzz"
#         if len(chFreq) == 1:
#             return True
        
# #         To check if all characters have same count
# #         If the count is 1 then return True else False
#         uniqueFreq = set(chFreq.values())
#         if len(uniqueFreq) == 1:
#             if uniqueFreq.pop() == 1:
#                 return True
#             else:
#                 return False
        
#         For every character in the word remove each character
#         Then check if the remaining word satisfies the given condition
        for i in range(len(word)):
            if self.check(word[:i] + word[i+1:]):
                return True
        return False
                    