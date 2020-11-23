s = input()
integers = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
class Solution:
    def __init__(self, s):
        self.s = s
    def romanToInt(self,s: str):
        result = 0
        for i, c in enumerate(s):
            if i + 1 < len(s) and integers[s[i]] < integers[s[i + 1]]:
                result -= integers[s[i]]
            else:
                result += integers[s[i]]
        return str(result)
print(Solution.romanToInt(s,s))