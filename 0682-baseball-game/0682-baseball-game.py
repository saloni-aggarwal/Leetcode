class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        for operation in operations:
            if operation == 'D':
                # prev = score.pop()
                # score.append(prev)
                score.append(2*score[-1])
            elif operation == 'C':
                score.pop()
            elif operation == '+':
                if len(score) >= 2:
                    # first = score.pop()
                    # second = score.pop()
                    # score.append(second)
                    # score.append(first)
                    score.append(score[-1] + score[-2])
            else:
                score.append(int(operation))
        return sum(score)