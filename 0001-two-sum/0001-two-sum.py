class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_indices = {}  # A dictionary to store the index of each number

        for i, num in enumerate(nums):
            complement = target - num

            # Check if the complement is already in the dictionary
            if complement in num_indices:
                return [num_indices[complement], i]

            # If not, add the current number and its index to the dictionary
            num_indices[num] = i

        
        return None


solution_instance = Solution()
print(solution_instance.twoSum([2,7,11,15], 9))  
print(solution_instance.twoSum([3,2,4], 6))      
print(solution_instance.twoSum([3,3], 6))        
