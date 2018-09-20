def parttion(data, left, right):
	key = data[left]
	low = left
	high = right
	while low < high:
		while (low < high) and (data[high] >= key):
			high -= 1
		if low < high:
			data[low] = data[high]
			low += 1
		while (low < high) and (data[low] <= key):
			low += 1
		if low < high:
			data[high] = data[low]
			high -= 1
		data[low] = key
	return low

def quicksort(data, left, right):
	if left < right:
		p = parttion(data, left, right)
		quicksort(data, left, p-1)
		quicksort(data, p+1, right)
	return data

li = [72, 6, 57, 88, 60, 42, 83, 73, 48, 85]
print(li)
quicksort(li, 0, len(li)-1)
print(li)