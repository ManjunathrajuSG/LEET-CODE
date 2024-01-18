class Solution(object):
    def numsSameConsecDiff(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        def generate_nums(curr_num, length):
            if length == n:
                result.append(int(curr_num))
                return

            last_digit = int(curr_num[-1])

            if last_digit + k <= 9:
                generate_nums(curr_num + str(last_digit + k), length + 1)
            if k > 0 and last_digit - k >= 0:
                generate_nums(curr_num + str(last_digit - k), length + 1)

        result = []
        
        # Start the recursion with digits from 1 to 9 (no leading zeros)
        for i in range(1, 10):
            generate_nums(str(i), 1)

        return result

# Example usage:
solution_instance = Solution()
print(solution_instance.numsSameConsecDiff(3, 7))  # Output: [181,292,707,818,929]
print(solution_instance.numsSameConsecDiff(2, 1))  # Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
