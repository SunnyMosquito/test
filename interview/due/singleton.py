# class Singleton(object):
#     def test(self):
#         print(self.__class__,'test')

# singletion = Singleton()

# datas = ['abcd'] * 1000000
# print(['abc']*2)
# string = ''
# import time

# start = time.time()
# string = ''.join(datas)
# end = time.time()
# print(end - start)


# start = time.time()
# for data in datas:
# 	string += data
# end = time.time()
# print(end - start)


# import time
# import sys
# def reverse(x):
#     """
#     :type x: int
#     :rtype: int
#     """
#     flag = False
#     if x < 0:
#         x = -x
#         flag = True
#     num = 0
#     while x != 0:
#         pop = x % 10
#         if num > 2**31 / 10 or (num > 2**31 / 10 and pop > 8):
#     	    return 0
#         if num < (-2**31 - 1) / 10 or (num < (-2**31 - 1) / 10 and pop < -7) :
#     	    return 0
#         num = num*10 + pop
#         x = x // 10
#     if flag:
#     	num = -num
#     return num
# print(reverse(-120))

# class Solution(object):
#     def isPalindrome(self, x):
#         """
#         :type x: int
#         :rtype: bool
#         """
#         if x < 0:
#         	return False
#         if x % 10 == 0 and x > 0:
#             return False
#         num = 0
#         while x > num:
#         	num = num*10 + x % 10
#         	x = x // 10
#         return x == num or x == num // 10

# class Solution:
#     def romanToInt(self, s):
#         """
#         :type s: str
#         :rtype: int IV
#         """
#         data = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
#         num = 0
#         for i in range(len(s)):
#             if i == len(s)-1 or data[s[i]] > data[s[i+1]]:
#                 num += data[s[i]]
#             else:
#                 num -= data[s[i]]
#         return num

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
        	return ''
        prefix = strs[0]
        for i in range(1,len(strs)):
        	while not strs[i].startswith(prefix):
        		prefix = prefix[:len(prefix)-1]
        		if prefix == '':
        			return ''
        return prefix
        


obj = Solution()
print(obj.longestCommonPrefix(['f','flr','flrt']))