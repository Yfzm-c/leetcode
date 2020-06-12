#有效的字母异位词

#给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
#示例 1:
#输入: s = "anagram", t = "nagaram"
#输出: true

#示例 2:
#输入: s = "rat", t = "car"
#输出: false
#说明:
#你可以假设字符串只包含小写字母。

#难渡：简单

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        for j in range(len(s)):
            if(s[j] not in t or s.count(s[j])!=t.count(s[j])):
                return False
        return True
solution=Solution()
s=input("请输入字符串s：")
t=input("请输入字符串t：")
print(solution.isAnagram(s,t))
