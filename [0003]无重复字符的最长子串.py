# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         charSet = set()
#         i = j = 0
#         maxLen = 0
#         while j < len(s):
#             while s[j] in charSet:
#                 charSet.remove(s[i])
#                 i += 1
#             while j < len(s) and s[j] not in charSet:
#                 charSet.add(s[j])
#                 j += 1
#             maxLen = max(maxLen, j - i)
#         return maxLen


class Solution:
    def lengthOfLongestSubstring(self, s):
        idxMap = {}
        i = 0
        maxLen = 0
        for j in range(len(s)):
            i = max(idxMap.get(s[j], -1) + 1, i)
            maxLen = max(maxLen, j - i + 1)
            idxMap[s[j]] = j
        return maxLen
