import random
def bubble_sort(nums):
	for i in range(len(nums)-1):
		for j in range(len(nums)-1-i):
			if nums[j] > nums[j+1]:
				nums[j], nums[j+1] = nums[j+1], nums[j]
			print(nums)

# def bubble_sort(nums):
# 	for i in range(len(nums)-1,-1,-1):
# 		for j in range(len(nums)-1,len(nums)-1-i,-1):
# 			if nums[j] > nums[j-1]:
# 				nums[j], nums[j-1] = nums[j-1], nums[j]
# 			print(nums)

nums = [random.randint(1, 10) for i in range(10)]
bubble_sort(nums)
print(nums)