'''
504. 七进制数
给定一个整数 num，将其转化为 7 进制，并以字符串形式输出。

示例 1:
输入: num = 100
输出: "202"

示例 2:
输入: num = -7
输出: "-10"


提示：
-107 <= num <= 107

https://leetcode-cn.com/problems/base-7
'''

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        negative = num < 0
        num = abs(num)
        res = []
        while num:
            res.append(str(num % 7))
            num = num // 7
        if negative:
            res.append('-')
        return ''.join(res[::-1])


m = Solution()
print(m.convertToBase7(100))
