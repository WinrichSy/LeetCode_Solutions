#Group Anagrams
#https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for i in strs:
            # print(i)
            sorted_str = ''.join(sorted(i))
            if sorted_str not in dictionary.keys():
                dictionary[sorted_str] = [i]
            elif sorted_str in dictionary.keys():
                dictionary[sorted_str].append(i)

        return([i for i in dictionary.values()])
