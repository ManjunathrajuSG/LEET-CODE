class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        elif n == 2:
            return 2

        # Initialize an array to store the number of ways to reach each step
        ways = [0] * (n + 1)
        ways[1] = 1
        ways[2] = 2

        # Use dynamic programming to fill in the array
        for i in range(3, n + 1):
            ways[i] = ways[i - 1] + ways[i - 2]

        return ways[n]

# Example usage:
solution_instance = Solution()
print(solution_instance.climbStairs(2))  # Output: 2
print(solution_instance.climbStairs(3))  # Output: 3
