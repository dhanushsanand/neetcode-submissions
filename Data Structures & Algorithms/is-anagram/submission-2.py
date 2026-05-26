class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        charList = [0]*26

        for c in range(len(s)):
            charList[ord(s[c])-ord('a')]+=1
            charList[ord(t[c])-ord('a')]-=1
        
        for value in charList:
            if value:
                return False
        return True

        # hashmap_s = {}
        # hashmap_t = {}
        # for c in s:
        #     if c in hashmap_s:
        #         hashmap_s[c]+=1
        #     else:
        #         hashmap_s[c]=1
        # for c in t:
        #     if c in hashmap_t:
        #         hashmap_t[c]+=1
        #     else:
        #         hashmap_t[c]=1
        # return True if hashmap_s == hashmap_t else False
        #Method 1
        # list_s = sorted(s)
        # list_t = sorted(t)
        # print(list_s)
        # print(list_t)
        # return True if list_s == list_t else False
        