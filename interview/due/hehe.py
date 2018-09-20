# def isValid(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         d = {'{':'}','[':']','(':')'}
#         stack = []
#         for c in s:
#             if c in d:
#                 stack.append(c)
#             else:
#                 if not stack or d[stack.pop()] != c:
#                     return False
#         if stack:
#             return False
#         else:
#             return True


# print(isValid('he','({}){}'))

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = merge = ListNode(0)
        print(l1.val,l2.val)
        while l1 and l2:
        	print(merge.val)
        	if l1.val > l2.val:
        		merge.next = l2
        		l2 = l2.next
        	else:
        		merge.next = l1
        		l1 = l1.next
        	merge = merge.next
        merge.next = l1 or l2
        return result.next
p = l1 = ListNode(1)
l1.next = ListNode(3)
l1 = l1.next
l1.next = ListNode(4)
l1 = l1.next
l1 = p

q = l2 = ListNode(1)
l2.next = ListNode(2)
l2 = l2.next
l2.next = ListNode(4)
l2 = l2.next
l2 = q
while l1:
	print(l1.val)
	l1 = l1.next

while l2:
	print(l2.val)
	l2 = l2.next
l1=p
l2=q
solution = Solution()

result = solution.mergeTwoLists(l1, l2)

while result:
	print(result.val)
	result = result.next