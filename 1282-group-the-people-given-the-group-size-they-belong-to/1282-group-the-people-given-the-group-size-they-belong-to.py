class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = {}
        for i in range(len(groupSizes)):
            if groupSizes[i] not in groups:
                groups[groupSizes[i]] = []
            groups[groupSizes[i]].append(i)
        
        output = []
        
        for group in groups:
            n = len(groups[group])
            temp = []
            for i in range(n):
                temp.append(groups[group][i])
                if ((i+1) % group) == 0:
                    output.append(temp.copy())
                    temp.clear()
        return output
            
            
            