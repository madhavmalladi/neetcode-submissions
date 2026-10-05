class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while (len(stones) > 1):
            sortedArr = sorted(stones)
            heaviest = sortedArr[-1]
            second = sortedArr[-2]
            if (heaviest == second):
                stones.remove(sortedArr[-1])
                stones.remove(sortedArr[-2])
            else:
                stones.remove(sortedArr[-2])
                stones[stones.index(heaviest)] = heaviest - second
        if (stones):
            return stones[0]
        else:
            return 0