#移除元素

#给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
#不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
#元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

#示例 2:
#给定 nums = [0,1,2,2,3,0,4,2], val = 2,
#函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。
#注意这五个元素可为任意顺序。
#你不需要考虑数组中超出新长度后面的元素。

#难度：简单

from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count=0
        j=len(nums)
        for i in range(j-1,-1,-1):
            if(nums[i]==val):
                nums.remove(nums[i])
                count+=1
        result=j-count
        return result

solution=Solution()
a=input("请输入一组数，以逗号隔开：")
b=int(input("请输入一个目标数："))
a=a.split(",")
nums=[int(a[i]) for i in range(len(a))]
print(solution.removeElement(nums,b))
