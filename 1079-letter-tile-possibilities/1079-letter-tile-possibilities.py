class Solution:
    ans = 0
    def tiles(self, counts):
        Solution.ans += 1
        for cnt in counts:
            if counts[cnt] > 0:
                counts[cnt] -= 1
                self.tiles(counts)
                counts[cnt] += 1
                
    def numTilePossibilities(self, tiles: str) -> int:
        counts = Counter(tiles)
        Solution.ans = 0
        self.tiles(counts)
        return Solution.ans - 1
        
        