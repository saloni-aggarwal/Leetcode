class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        # print(operations[2].isdigit())
        for operation in operations:
            print("score =", score)
            # if operation.isdigit():
            #     score.append(int(operation))
            if operation == 'D':
                prev = score.pop()
                score.append(prev)
                score.append(2*prev)
            elif operation == 'C':
                score.pop()
            elif operation == '+':
                if len(score) >= 2:
                    first = score.pop()
                    second = score.pop()
                    score.append(second)
                    score.append(first)
                    score.append(first + second)
            else:
                score.append(int(operation))
        return sum(score)