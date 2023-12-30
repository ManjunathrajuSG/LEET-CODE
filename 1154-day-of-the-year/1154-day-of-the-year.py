class Solution:
    def dayOfYear(self, date: str) -> int:
        # Split the input date into year, month, and day
        year, month, day = map(int, date.split('-'))
        
        # List of days in each month
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        # Check for leap year and update days in February
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            days_in_month[2] = 29
        
        # Calculate the day number
        day_number = sum(days_in_month[:month]) + day
        
        return day_number

# Test examples
solution = Solution()
print(solution.dayOfYear("2019-01-09"))  # Output: 9
print(solution.dayOfYear("2019-02-10"))  # Output: 41
