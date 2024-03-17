class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_anagram = {}
        t_anagram = {}

        for i in range(len(s)):
            if s[i] in s_anagram: 
                s_anagram[s[i]] += 1
            else:
                s_anagram[s[i]] = 1

        for j in range(len(t)):
            if t[j] in t_anagram: 
                t_anagram[t[j]] += 1
            else:
                t_anagram[t[j]] = 1
        if s_anagram == t_anagram: 
            return True 
        else: 
            return False
        
#or you can sort it and see if it equals each other 
        
        #return sorted(s) == sorted(t)