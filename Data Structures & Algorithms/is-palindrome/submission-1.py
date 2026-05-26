class Solution:
    # letter = ""

        # for c in s:
        #     if str.isalnum(c):
        #         letter +=c
        # letter = str.lower(letter)
        # first = 0
        # last = len(letter)-1

        # while first< last:
        #     if letter[first] == letter[last]:
        #         first +=1
        #         last -=1
        #     else:
        #         return False
        # return True
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            while l<r and not self.alphaNum(s[l]):
                l+=1
            while r>l and not self.alphaNum(s[r]):
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l,r = l+1,r-1
        return True
    def alphaNum(self,c):
        return (ord('A')<=ord(c)<=ord('Z') or 
                ord('a')<=ord(c)<=ord('z') or 
                ord('0')<=ord(c)<=ord('9'))

        