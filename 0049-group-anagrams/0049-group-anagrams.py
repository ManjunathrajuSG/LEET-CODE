class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_groups = {}

        for word in strs:
            # Sort the characters of the word
            sorted_word = ''.join(sorted(word))

            # Add the word to its corresponding anagram group
            if sorted_word in anagram_groups:
                anagram_groups[sorted_word].append(word)
            else:
                anagram_groups[sorted_word] = [word]

        return list(anagram_groups.values())

# Example usage:
solution_instance = Solution()
print(solution_instance.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
print(solution_instance.groupAnagrams([""]))
# Output: [[""]]
print(solution_instance.groupAnagrams(["a"]))
# Output: [["a"]]
