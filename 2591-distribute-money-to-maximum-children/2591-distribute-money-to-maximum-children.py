class Solution:
    def distMoney(self, money: int, children: int) -> int:
        money -= children
        if money < 0:
            return -1
        elif money == 0:
            return 0
        elif money//7 == children and money%7 == 0:
            return children
        elif money//7 == children-1 and money%7 == 3:
            return children-2
        # else:
        return min(children-1, money//7)
        