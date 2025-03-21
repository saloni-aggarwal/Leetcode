class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            flowerbed[0] = 1
            n -= 1 
        if len(flowerbed) >= 2:
            if flowerbed[0] == flowerbed[1] == 0:
                flowerbed[0] = 1
                n -= 1
            if flowerbed[-1] == flowerbed[-2] == 0:
                flowerbed[-1] = 1
                n -= 1 
        for i in range(1,len(flowerbed)-1):           
            if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
        
        return True if n <= 0 else False
        