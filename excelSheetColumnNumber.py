#给定一个Excel表格中的列名称，返回其相应的列序号。
#例如
#    A -> 1
#    B -> 2
#    C -> 3
#    ...
#    Z -> 26
#    AA -> 27
#    AB -> 28 
#    ...
#示例：输入: "AB"   输出: 28
#难度：简单


class Solution:
    def titleToNumber(self, s: str) -> int:
        result=0
        for i in range(len(s)-1,-1,-1):
            result+=(ord(s[i])-64)*pow(26,len(s)-1-i)
        return result
solution=Solution()
s=input("请输入一个字符串：")
print(solution.titleToNumber(s))
