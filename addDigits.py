#给定一个非负整数num，反复将各个位上的数字相加，直到结果为一位数
#实例：输入38   输出2
class Solution:
    def addDigits(self, num: int) -> int:
        a=str(num)
        while(len(a)>1):
            b=0
            for i in range(len(a)):
                b+=eval(a[i])
            a=str(b)
        result=eval(a)
        return result

solotion=Solution()
num=eval(input("请输入一个非负整数："))
print("结果为：%d"%(solotion.addDigits(num)))
