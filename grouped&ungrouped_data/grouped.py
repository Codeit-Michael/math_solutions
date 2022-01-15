# for grouped data
class mean():
	# total_fx = ∑𝑓𝑋
	# N = 𝑁 

	def __init__(self,f:list,x:list):
		self.f = f
		self.x = x
		self.fx = []

	def fx_finder(self):
		for i in range(0,len(self.f)):
			new = (self.f[i] * self.x[i])
			self.fx.append(new)
		return self.fx

	def get_mean(self):
		total_fx = sum(self.fx)
		N = sum(self.f)
		mean_answer = total_fx/N
		return mean_answer


if __name__ == '__main__':
	f = [3,5,9,12,5,4,2]
	x = [122,131,140,149,158,167,176]

	d1 = mean(f,x)
	print(d1.fx_finder())
	print(d1.get_mean())


class median():
	pass


class mode():
	pass