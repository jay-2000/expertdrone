# 1823. Find the Winner of the Circular Game(Medium)

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        new_list = list(range(1,n+1))
        while len(new_list)>1:
            i = (k-1)%len(new_list)
            new_list.pop(i)
            new_list = new_list[i:]+new_list[:i]
        return new_list[0]