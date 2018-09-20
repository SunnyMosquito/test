# class Solution:
#     def merge(self, nums1, m, nums2, n):
#         """
#         :type nums1: List[int]
#         :type m: int
#         :type nums2: List[int]
#         :type n: int
#         :rtype: void Do not return anything, modify nums1 in-place instead.
#         """
#         i = 0
#         j = 0
#         if nums1[0] > nums2[-1]:
#             for i in range(n-1,-1,-1):
#                 nums1.insert(0,nums2[i])
#                 del nums1[-1]
#             return
#         if nums1[m-1] < nums2[0]:
#             for i in range(m,m+n):
#                 nums1.insert(i,nums2[j])
#                 j += 1
#                 del nums1[-1]
#             return
#         while i < m+n-1  and j < n:
#             if nums1[i] > nums2[j]:
#                 nums1.insert(i, nums2[j])
#                 del nums1[-1]
#                 i += 1
#                 j += 1
#             else:
#                 i += 1
#         if j < n:
#             for a in range(m+j,len(nums1)):
#                 nums1[a] = nums2[j]
#                 j += 1

# nums1 = [4,0,0,0,0,0]
# nums2 = [1,2,3,5,6]
# solution = Solution()
# solution.merge(nums1, 1, nums2,5)
# print(nums1)
# -*- coding: utf-8 -*-
 
"""
    【简介】
    水平布局管理例子
    
    
"""

import sys
from PyQt5.QtWidgets import QApplication  ,QWidget ,QHBoxLayout , QPushButton

class Winform(QWidget):
    def __init__(self,parent=None):
        super(Winform,self).__init__(parent)
        self.setWindowTitle("水平布局管理例子") 
    
        # 水平布局按照从左到右的顺序进行添加按钮部件。
        hlayout = QHBoxLayout()       
        hlayout.addWidget( QPushButton(str(1)))
        hlayout.addWidget( QPushButton(str(2)))
        hlayout.addWidget( QPushButton(str(3)))
        hlayout.addWidget( QPushButton(str(4)))        
        hlayout.addWidget( QPushButton(str(5)))        
        self.setLayout(hlayout)   
  
if __name__ == "__main__":  
        app = QApplication(sys.argv) 
        form = Winform()
        form.show()
        sys.exit(app.exec_())