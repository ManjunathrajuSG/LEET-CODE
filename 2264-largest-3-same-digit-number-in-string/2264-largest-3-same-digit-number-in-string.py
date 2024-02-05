import re
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        l1 = ['111', '222', '333', '444', '555', '666', '777', '888', '999', '000']
        res = []
        int_arr = []

        for i in range(len(num) - 2):
            if num[i:i + 3] in l1:
                res.append(num[i:i + 3])

        if not res:
            return ""

        if all(int(x) == 0 for x in res):
            return '000'

        for i in res:
            int_arr.append(int(i))

        res = max(int_arr)
        return str(res)
