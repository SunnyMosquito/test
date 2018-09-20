import random

nums = [random.randint(1,50) for i in range(10)]

def select_sort(nums):
	for i in range(len(nums)-1):
		min_index = i
		for j in range(i+1,len(nums)):
			if nums[min_index] > nums[j]:
				nums[min_index], nums[j] = nums[j], nums[min_index]
			print(i,j,nums)

select_sort(nums)