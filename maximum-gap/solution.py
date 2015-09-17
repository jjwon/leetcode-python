from math import ceil

class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # corner case as defined by the problem
        if len(nums) < 2:
            return 0

        # grab the min and max elements, and compute bucket size
        min_val = min(nums)
        max_val = max(nums)
        bucket_size = int(ceil(float((max_val - min_val)) / (len(nums)))) # need to round up

        # if all elements are the same, there is no gap
        if bucket_size == 0: return 0

        # put elements in buckets
        buckets = [[] for _ in range((max_val-min_val)/bucket_size+1)]
        for num in nums:
            buckets[(num-min_val)/bucket_size].append(num)

        # starting from the second bucket, start hunting for gaps
        i = 1
        gap = 0
        lower = max(buckets[0])
        while i < len(buckets):
            bucket = buckets[i]
            i += 1

            if len(bucket) == 0: continue
            if min(bucket) - lower > gap:
                gap = min(bucket) - lower
            lower = max(bucket)

        return gap

if __name__ == "__main__":
    print Solution().maximumGap([1, 1, 1, 1, 1, 5, 5, 5, 5, 5])
