class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # Count occurrences of each letter in the text
        counts = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}

        for char in text:
            if char in counts:
                counts[char] += 1

        # Calculate the maximum number of instances of "balloon"
        counts['l'] //= 2
        counts['o'] //= 2

        return min(counts.values())

# Test examples
solution = Solution()
print(solution.maxNumberOfBalloons("nlaebolko"))  # Output: 1
print(solution.maxNumberOfBalloons("loonbalxballpoon"))  # Output: 2
print(solution.maxNumberOfBalloons("leetcode"))  # Output: 0
