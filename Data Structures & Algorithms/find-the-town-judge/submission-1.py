class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        people = set([i for i in range(1, n + 1)])

        for t in trust:
            if t[0] in people:
                people.remove(t[0])

        if len(people) != 1:
            return -1

        judge = people.pop()
        
        people = set([i for i in range(1, n + 1)])
        people.remove(judge)

        for t in trust:
            if t[1] == judge:
                people.remove(t[0])

        if not people:
            return judge
        else:
            return -1