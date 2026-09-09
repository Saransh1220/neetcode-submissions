class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        anagram = {}
        for letter in s:
            if letter in anagram:
                anagram[letter] += 1
            else:
                anagram[letter] = 1
        
        for letter in t:
            if letter not in anagram:
                return False
            anagram[letter] -= 1
            if anagram[letter]<0:
                return False
            
        return True