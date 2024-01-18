class Solution:
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        char_counts = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}

        # Count occurrences of each character in text
        for char in text:
            if char in char_counts:
                char_counts[char] += 1

        # Calculate the maximum number of instances of "balloon" that can be formed
        char_counts['l'] //= 2  # Each instance of "balloon" requires two 'l' characters
        char_counts['o'] //= 2  # Each instance of "balloon" requires two 'o' characters

        return min(char_counts.values())


solution_instance = Solution()
print(solution_instance.maxNumberOfBalloons("nlaebolko")) 
print(solution_instance.maxNumberOfBalloons("loonbalxballpoon"))  
print(solution_instance.maxNumberOfBalloons("leetcode"))  
