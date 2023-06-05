from collections import defaultdict

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        bombsGraph = defaultdict(list)
        n = len(bombs)
        
        for i in range(n):
            x1, y1, r1 = bombs[i]
            for j in range(i+1, n):
                
                x2, y2, r2 = bombs[j]
                dist = ((x1 - x2) ** 2) + ((y1 - y2) ** 2)
                
                if r1 ** 2 >= dist:
                    bombsGraph[i].append(j)
                    
                if r2 ** 2 >= dist:
                    bombsGraph[j].append(i)
                    
        def dfs(curr, visited):
            visited.add(curr)
            for nei in bombsGraph[curr]:
                if nei not in visited:
                    dfs(nei, visited)
                    
            return len(visited)
        
        ans = 0
        for i in range(n):
            visited = set()
            ans = max(ans, dfs(i, visited))
        
        return ans