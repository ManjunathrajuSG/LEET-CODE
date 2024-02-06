class Solution:
    def reverseWords(self, s: str) -> str:
        sb = list(s)
        i = 0
        j = 0

        while i < len(sb):
            while i < j or (i < len(sb) and sb[i] == ' '):
                i += 1
            while j < i or (j < len(sb) and sb[j] != ' '):
                j += 1
            self.reverse(sb, i, j - 1)

        return ''.join(sb)

    def reverse(self, sb, l, r):
        while l < r:
            sb[l], sb[r] = sb[r], sb[l]
            l += 1
            r -= 1

