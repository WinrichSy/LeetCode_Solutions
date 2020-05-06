#Longest Palindromic Substring
#https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def reverse(self, word):
        return word[::-1]

    def longestPalindrome(self, s: str) -> str:
        if len(s)==1:
            return s
        elif s=='':
            return ''

        max_word = ''
        max_length = 0
        for i in range(len(s)-1):
            j = len(s)-1

            while(j>i):
                #Check to see if first letter and last letter are the same
                #If not, then continue to the next i
                if s[i] != s[j]:
                    j -= 1
                    continue

                word = s[i:j+1]
                if word == self.reverse(word):
                    word_length = len(word)
                    if word_length > max_length:
                        max_length = word_length
                        max_word = word
                    j -= 1

                j -= 1

        if max_length==0:
            return s[0]

        return max_word
