#基本计算器
"""
实现一个基本的计算器来计算一个简单的字符串表达式的值。
字符串表达式可以包含左括号 ( ，右括号 )，加号 + ，减号 -，非负整数和空格  。
示例 :
输入: "(1+(4+5+2)-3)+(6+8)"
输出: 23
"""
#难度：困难

class Solution:
    def calculate(self, s: str) -> int:
        s=s.replace(' ','')
        stack=[]
        flag=1
        i=0
        result=0
        stack.append(1)
        while(i<len(s)):
            if(s[i]=='+'):
                flag=1
                i+=1
            elif(s[i]=='-'):
                flag=-1
                i+=1
            elif(s[i]=='('):
                stack.append(flag*stack[-1])
                flag=1
                i+=1
            elif(s[i]==')'):
                stack.pop()
                i+=1
            else:
                num=''
                while(i<len(s)and s[i].isdigit()):
                    num+=s[i]
                    i+=1
                result+=int(num)*flag*stack[-1]
        return result

soution=Solution()
a=input("请输入你所要计算的式子：")
print(soution.calculate(a))
