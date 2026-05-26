class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_s = sorted(s)
        list_t = sorted(t)

        return True if list_s == list_t else False
        