#Z 字形变换
#难度：中等

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows==1):
            return s
        m=0
        n=0
        flag=0
        result=""
        a=[['0' for i in range(len(s))] for j in range(numRows)]
        for k in range(len(s)):
            a[m][n]=s[k]
            if(m==0):
                flag=0
            elif(m==numRows-1):
                flag=1
            if(flag==0):
                m+=1
            elif(flag==1):
                m-=1
                n+=1
        q=0
        w=0
        for q in range(numRows):
            for w in range(len(s)):
                if(a[q][w]!='0'):
                    result+=a[q][w]
        return result
solution=Solution()
a=input("请输入一个字符串：")
b=int(input("请输入一个数字："))
print(solution.convert(a,b))
