class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hashmap = {}
        for a in s:
            if a in hashmap:
                hashmap[a]+=1
            else:
                hashmap[a] = 1
        
        for b in t:
            if b not in hashmap:
                return False
            if hashmap[b] <=0:
                return False
            hashmap[b] -= 1
        return True

