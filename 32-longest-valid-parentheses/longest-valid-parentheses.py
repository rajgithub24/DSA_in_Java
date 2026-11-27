class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left, right, max_length = 0, 0, 0
        for x in s:
            if x is '(':
                left+= 1
            else:
                right+= 1
            if left == right:
                max_length = max(max_length, left + right)
            elif right > left:
                left = right = 0
        left = right = 0
        for x in s[::-1]:
            if x is '(':
                left+= 1
            else:
                right+= 1
            if left == right:
                max_length = max(max_length, left + right)
            elif left > right:
                left = right = 0
        return max_length
        