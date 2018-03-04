def quicksort(l):
	if len(l) < 2:
		return(l)
	pivot = [l[0]]
	less = []
	greater = []
	for num in range(1, len(l)):
		if l[num] < pivot[0]:
			less.append(l[num])
		elif l[num] > pivot[0]:
			greater.append(l[num])
		else:
			pivot.append(l[num])
	return(quicksort(less) + pivot + quicksort(greater))
