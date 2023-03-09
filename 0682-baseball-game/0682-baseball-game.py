class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        
        for operation in operations:
            if operation == 'D':
                score.append(2*score[-1])
            elif operation == 'C':
                score.pop()
            elif operation == '+':
                if len(score) >= 2:
                    score.append(score[-1] + score[-2])
            else:
                score.append(int(operation))
                
        return sum(score)