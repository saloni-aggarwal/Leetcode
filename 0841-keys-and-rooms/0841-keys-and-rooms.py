class Solution:
    def visitAll(self, rooms, key, visited):
        visited.add(key)
        
        for k in rooms[key]:
            if k not in visited:
                self.visitAll(rooms, k, visited)
                
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        visited.add(0)
        for key in rooms[0]:
            if key not in visited:
                self.visitAll(rooms, key, visited)
                
        for i in range(len(rooms)):
            if i not in visited:
                return False
        return True
                