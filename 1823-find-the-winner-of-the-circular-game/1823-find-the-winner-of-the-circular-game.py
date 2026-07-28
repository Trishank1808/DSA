class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        player=[]
        for i in range(1,n+1):
            player.append(i)
        index=0
        while len(player)>1:
            index=(index +k-1)%len(player)
            player.pop(index)
        return player[0]
