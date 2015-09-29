class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # initialize a dp matrix
        # note that this matrix is padded by one, so dp[0][0] refers to matching empty string against empty string
        dp = [[0]*(len(word2)+1) for _ in range(len(word1)+1)]

        # base case: an empty second string requires i deletions
        for i in range(len(word1)+1):
            dp[i][0] = i

        # base case: an empty first string requires j insertions
        for j in range(len(word2)+1):
            dp[0][j] = j

        # fill out the dp matrix
        for j in range(1, len(word2)+1):
            for i in range(1, len(word1)+1):
                if word1[i-1] == word2[j-1]:
                    # if there's a match
                    dp[i][j] = dp[i-1][j-1]
                # no match: compare mismatch penalty, insertion penalty, and deletion penalty
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

        return dp[len(word1)][len(word2)]
