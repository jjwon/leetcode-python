class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # initialize count to 0, and iterate over all bits
        count = 0
        for i in range(32):
            # if the ith bit is turned on, increase count
            if ((1 << i) & n) > 0:
                count += 1

        return count
