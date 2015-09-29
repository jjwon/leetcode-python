class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # shortcut ending for edge case
        if not digits: return []

        # initialize mapping for keypad, where the ith element has the correct letters.
        mapping = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        # initialize a list to hold the results, and perform dfs
        results = []
        self.letterCombRecur(digits, mapping, [], results)
        return results

    def letterCombRecur(self, digits, mapping, intermediate, results):
        # if we have finished generating a string, append it to the results
        if len(digits) == len(intermediate):
            results.append(''.join(intermediate))
            return

        # iterate over all potential next letters, append, recurse, and reset
        for letter in mapping[int(digits[len(intermediate)])]:
            intermediate.append(letter)
            self.letterCombRecur(digits, mapping, intermediate, results)
            intermediate.pop(-1)

if __name__ == "__main__":
    for i in ["23"]:
        print Solution().letterCombinations(i)
