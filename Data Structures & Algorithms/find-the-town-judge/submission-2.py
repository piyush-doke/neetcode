class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inDegree = [0] * (n + 1)
        outDegree = [0] * (n + 1)

        for t in trust:
            inDegree[t[1]] += 1
            outDegree[t[0]] += 1

        for i in range(1, n + 1):
            if inDegree[i] == n - 1 and outDegree[i] == 0:
                return i

        return -1