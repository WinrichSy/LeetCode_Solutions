#Longest Substring Without Repeating Characters
#https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        seen_letters = []
        for i in s:
            if i not in seen_letters:
                seen_letters.append(i)
                if len(seen_letters)>max_length:
                    max_length = len(seen_letters)

            elif i in seen_letters:
                seen_letters = seen_letters[seen_letters.index(i)+1:]
                seen_letters.append(i)


        return max_length
