class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        
        def traverse(node, arr, dist):
            if node != -1 and arr[node] == -1:
                arr[node] = dist
                traverse(edges[node], arr, dist+1)
            return arr
        n = len(edges)
        arr1 = [-1] * n
        arr2 = [-1] * n
        arr1 = traverse(node1, arr1, 0)
        arr2 = traverse(node2, arr2, 0)
        
        minDist = float('inf')
        minEle = -1
        for i in range(n):
            if arr1[i] != -1 and arr2[i] != -1:
                dist = max(arr1[i], arr2[i])
                if dist < minDist:
                    minEle = i
                    minDist = dist
                    
        return minEle