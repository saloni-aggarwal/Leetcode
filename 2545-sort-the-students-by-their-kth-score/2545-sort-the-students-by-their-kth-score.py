class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        for i in range(len(score)):
            arr.append(score[i][k])
        arr = sorted(enumerate(arr), key = lambda x: x[1], reverse=True)
        output = []
        for idx, val in arr:
            output.append(score[idx])
        return output
            