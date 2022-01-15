# for ungrouped data
def mean(x:list):
	message = f'total: {sum(x)},\nlength: {len(x)},\nmean: {sum(x)/len(x)}'
	return (message)


def median(x:list):
	length = len(x)
	mid = len(x)//2
	if (length % 2) == 0:
		combine = x[mid-1] + x[mid]
		return f'even, mid is {combine/2}'
	else:
		return f'odd, mid is {x[mid]}'


class mode():
	def __init__(self,numlist:list):
		self.numlist = numlist
		self.nums_mode = {}

	def mode_lister(self):
		for x in self.numlist:
			if x not in self.nums_mode:
				self.nums_mode[x] = 0
			self.nums_mode[x] += 1
		return self.nums_mode

	def biggest_mode(self):
		my_mode = None
		n1 = 0
		for x in self.nums_mode:
			if self.nums_mode[x] > n1:
				n1 = self.nums_mode[x]
				my_mode = f'{x}: {self.nums_mode[x]}'
		return my_mode


if __name__ == '__main__':
	numba = [21,16,14,11,9,8,7]
	nums = [16,16,19,21,21,23,24,24,26,26,26,26,26,27,27,27,28,28,29,29,29,32,34,34,34,35,35,38,38,38,41,42,43,45,46,46,48,48,51,51,52,54,56,58,59,60,62,64]

	print(mean(nums))

	print(median(nums))

	f1 = mode(nums)
	print(f1.mode_lister())
	print(f1.biggest_mode())