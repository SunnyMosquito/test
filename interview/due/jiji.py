# def plusOne(digits):
#     """
#     :type digits: List[int]
#     :rtype: List[int]
#     """
#     if digits == []:
#         return []
#     sum = digits[-1] + 1
#     if sum > 9:
#         j = len(digits) - 2
#         digits[-1] = 0
#         a = 1
#         while j >= 0:
#             sum = digits[j] + a
#             digits[j] = sum % 10
#             a = sum // 10
#             j -= 1
#             print(a)
#         if a > 0:
#             digits = [a] + digits
#             print(1)
#         return digits            
#     digits[-1] = sum
#     return digits
# print(plusOne([8,9,9]))

def addBinary(a, b):
    # if a == '':
    #     return a
    # if b == '':
    #     return b
    # i = len(a) - 1
    # j = len(b) - 1
    # result = []
    # n = 0
    # m = 0
    # while i >= 0 or j >= 0:
    #     iv = int(a[i]) if i >= 0 else 0
    #     jv = int(b[j]) if j >= 0 else 0
    #     sum = iv + jv + m
    #     n = sum % 2
    #     m = sum // 2
    #     print(n, m)
    #     i -= 1
    #     j -= 1
    #     result.insert(0, n)
    # if m > 0:
    #     result.insert(0, m)
    # return str(result)
    return str(bin(int(a, 2) + int(b, 2)))
print(addBinary('11','1'))