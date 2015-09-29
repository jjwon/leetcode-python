class SolutionOne(object):

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_list, t_list = list(s), list(t)
        return sorted(s_list) == sorted(t_list)


class SolutionTwo(object):

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        from collections import Counter 
        return Counter(s) == Counter(t)


class SolutionThree(object):

    from functools import reduce
    import string
    alpha = list(string.lowercase)    
    primes = [ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    alpha_to_prime = dict(zip(alpha, primes))

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return  self.hash(s) ==  self.hash(t)
    

    def hash(self, string):
        prime_factors = [self.alpha_to_prime[char] for char in string]
        return reduce(lambda x,y: x*y, prime_factors, 1)



if __name__ == "__main__":
    print SolutionOne().isAnagram("dog", "god")
    print SolutionTwo().isAnagram("dog", "god")
    print SolutionThree().isAnagram("dog", "god")
