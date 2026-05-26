class Solution:
    def isPalindrome(self, s: str) -> bool:
        letter = ""

        for c in s:
            if str.isalnum(c):
                letter +=c
        letter = str.lower(letter)
        first = 0
        last = len(letter)-1

        while first< last:
            if letter[first] == letter[last]:
                first +=1
                last -=1
            else:
                return False
        return True
        