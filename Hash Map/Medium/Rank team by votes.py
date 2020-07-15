class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        n = len(votes[0])
        d = {v:[n]*n + [v] for v in votes[0]}
        for vote in votes:
            for i,v in enumerate(vote):
                d[v][i] -= 1
        return ''.join(sorted(votes[0],key=d.get))
