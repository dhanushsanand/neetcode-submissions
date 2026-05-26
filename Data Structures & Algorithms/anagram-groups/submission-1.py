from typing import DefaultDict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = DefaultDict(list)
        for word in strs:
            count = [0]*26
            for c in word:
                count[ord(c)-ord("a")]+=1
            hashmap[tuple(count)].append(word)
        
        return list(hashmap.values())


        # hashmap = DefaultDict(list)

        # for s in strs:
        #     count = [0]*26
        #     for c in s:
        #         count[ord(c)-ord('a')]+=1
        #     hashmap[tuple(count)].append(s)
        
        # return list(hashmap.values())
        