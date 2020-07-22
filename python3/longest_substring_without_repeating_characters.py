#
# Given a string, find the length of the longest substring without repeating characters.
#

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:        
        string_length = len(s)
        longest_substring = 0
        current_substring = {}
        i = 0
        j = 0
        while i < string_length:
            current_substring[s[i]] = current_substring.get(s[i], 0) + 1
            if len(current_substring) > longest_substring:
                longest_substring = len(current_substring)
            if current_substring[s[i]] > 1:
                current_substring = {}
                j += 1
                i = j-1
            i += 1
        return longest_substring


################################################################################
if __name__ == "__main__":
    pass
