from collections import Counter

class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Filter even numbers
        even_nums = [num for num in nums if num % 2 == 0]

        # If there are no even numbers, return -1
        if not even_nums:
            return -1

        # Count occurrences of each even number
        even_counts = Counter(even_nums)

        # Find the most frequent even number with the smallest value
        most_frequent_even = min(even_counts, key=lambda x: (-even_counts[x], x))

        return most_frequent_even

# Example usage:
solution_instance = Solution()
print(solution_instance.mostFrequentEven([0,1,2,2,4,4,1]))  # Output: 2
print(solution_instance.mostFrequentEven([4,4,4,9,2,4]))  # Output: 4
