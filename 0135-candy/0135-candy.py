class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n

        for i in range(1, n):
            prev = ratings[i - 1]
            if ratings[i] > prev:
                candies[i] = candies[i - 1] + 1
        for i in range(n - 2, -1, -1):
            next = ratings[i + 1]
            if ratings[i] > next:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        return sum(candies)