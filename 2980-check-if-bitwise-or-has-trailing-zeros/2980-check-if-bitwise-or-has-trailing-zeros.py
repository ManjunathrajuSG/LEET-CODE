class Solution(object):
    def hasTrailingZeros(self, nums):
        
        # Function to count trailing zeros in binary representation
        def countTrailingZeros(num):
            count = 0
            while num & 1 == 0 and num > 0:
                count += 1
                num >>= 1
            return count
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                # Bitwise OR of two elements
                bitwise_or_result = nums[i] | nums[j]
                if countTrailingZeros(bitwise_or_result) > 0:
                    return True
        return False


solution = Solution()
print(solution.hasTrailingZeros([1, 2, 3, 4, 5]))  
print(solution.hasTrailingZeros([2, 4, 8, 16]))     
print(solution.hasTrailingZeros([1, 3, 5, 7, 9]))    
