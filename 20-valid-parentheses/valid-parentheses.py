class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {
            "}" : "{", ")" : "(", "]" : "["
        }
        open_bracket = set(["(", "[", "{"])
        for x in s:
            if x in open_bracket:
                stack.append(x)
            elif stack and stack[-1] == bracket_map[x]:
                stack.pop()
            else:
                return False
        if stack:
            return False
        else:
            return True
        