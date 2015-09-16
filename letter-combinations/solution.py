class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits: return []

        mapping = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        results = []
        self.letterCombRecur(digits, mapping, [], results)
        return results

    def letterCombRecur(self, digits, mapping, intermediate, results):
        if len(digits) == len(intermediate):
            results.append(''.join(intermediate))
            return
        i = len(intermediate)
        for letter in mapping[int(digits[i])]:
            intermediate.append(letter)
            self.letterCombRecur(digits, mapping, intermediate, results)
            intermediate.pop(-1)

if __name__ == "__main__":
    for i in ["23"]:
        print Solution().letterCombinations(i)
