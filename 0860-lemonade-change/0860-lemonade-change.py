from collections import defaultdict
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0
        total = 0
        for bill in bills:
            # print("bill =", bill)
            
            if bill == 5:
                five += 1
            elif bill == 10:
                ten += 1
                if five > 0:
                    five -= 1
                else:
                    return False
            else:
                if five > 0 and ten > 0:
                    five -= 1
                    ten -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
#             changeToGive = bill - 5
#             if (changeToGive == 5) and changeLeft[5] > 0:
#                 changeLeft[5] -= 1
#                 changeToGive -= 5
                
#             if (changeToGive == 15):
#                 if changeLeft[10] > 0 and changeLeft[5] > 0:
#                     changeLeft[10] -= 1
#                     changeLeft[5] -= 1
#                     changeToGive -= 15
#                 elif changeLeft[5] == 3:
#                     changeLeft[5] -= 3
#                     changeToGive -= 15
                
#             if changeToGive != 0:
#                 return False
            # print("changeLeft =", changeLeft)
        return True
            
                
        