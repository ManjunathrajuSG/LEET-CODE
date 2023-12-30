from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Check which half is sorted
            if nums[left] <= nums[mid]:
                # Left half is sorted
                if nums[left] <= target <= nums[mid]:
                    # Target is in the left half
                    right = mid - 1
                else:
                    # Target is in the right half
                    left = mid + 1
            else:
                # Right half is sorted
                if nums[mid] <= target <= nums[right]:
                    # Target is in the right half
                    left = mid + 1
                else:
                    # Target is in the left half
                    right = mid - 1

        # If the target is not found
        return -1

# Example usage:
solution = Solution()
nums1 = [4, 5, 6, 7, 0, 1, 2]
target1 = 0
print(solution.search(nums1, target1))  # Output: 4

nums2 = [4, 5, 6, 7, 0, 1, 2]
target2 = 3
print(solution.search(nums2, target2))  # Output: -1

nums3 = [1]
target3 = 0
print(solution.search(nums3, target3))  # Output: -1
