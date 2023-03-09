class Solution:
    
    def gcd(self, x, y):
        if y > x:
            x, y = y, x
        while(y):
           x, y = y, x % y
        return abs(x)
    
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) == 1:
            return False
        
        lst = list(Counter(deck).values())
        
        if len(lst) == 1:
            return True
        
        g = self.gcd(lst[0], lst[1])
        if g == 1:
            return False
        
        for i in range(2, len(lst)):
            g = gcd(g, lst[i])
            if g == 1:
                return False
            
        return True