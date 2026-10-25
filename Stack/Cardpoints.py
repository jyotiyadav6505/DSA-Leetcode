class Solution(object):
    def maxScore(self, cardPoints, k):
        n = len(cardPoints)

        total = sum(cardPoints[:k])
        max_points = total

        for i in range(1, k + 1):
            total -= cardPoints[k - i]
            total += cardPoints[n - i]

            max_points = max(max_points, total)

        return max_points