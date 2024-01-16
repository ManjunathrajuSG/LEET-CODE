class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1

# Example usage
solution = Solution()

# Example 1
haystack1 = "sadbutsad"
needle1 = "sad"
print(solution.strStr(haystack1, needle1))  # Output: 0

# Example 2
haystack2 = "leetcode"
needle2 = "leeto"
print(solution.strStr(haystack2, needle2))  # Output: -1
