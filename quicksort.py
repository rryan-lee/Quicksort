def quicksort(l):
	if len(l) < 2:
		return(l)
	pivot = [l[0]]
	less = []
	greater = []
	for num in l[1:]:
		if num < pivot[0]:
			less.append(num)
		elif num > pivot[0]:
			greater.append(num)
		else:
			pivot.append(num)
	return(quicksort(less) + pivot + quicksort(greater))
