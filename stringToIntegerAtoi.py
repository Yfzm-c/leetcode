#字符串转换整数 (atoi)
#难度：中等

class Solution:
    def myAtoi(self, str: str) -> int:
        i=0
        flag=1
        result=0
        c={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0}
        while(i<len(str) and str[i]==" "):
            i=i+1
        if(i>=len(str) or str[i] not in ['1','2','3','4','5','6','7','8','9','0','+','-']):
            return 0
        elif str[i] == '+':
            i=i+1
        elif str[i] == '-':
            flag=-1
            i=i+1
        while(i<len(str)and str[i] in c):
            result=result*10+c[str[i]]
            i+=1
        result=flag*result
        if(result>pow(2,31)-1):
            return pow(2,31)-1
        elif(result<pow(-2,31)):
            return pow(-2,31)
        return result
solution=Solution()
a=input("请输入一个字符串：")
print(solution.myAtoi(a))
