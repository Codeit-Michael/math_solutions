from prettytable import PrettyTable

# for grouped data
class ClassInterval():
	def __init__(self,lowest:int,highest:int,class_size:int):
		self.lowest = lowest
		self.highest = highest+1
		self.class_size = class_size
		self.single_class = {}

		for x in range(self.lowest,self.highest,self.class_size):
			self.single_class[x] = []
			for y in range(x,x+self.class_size):
					self.single_class[x].append(y)

	def class_interval(self):
		return self.single_class


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


class median():
	# LT_cumf = < cum f
	pass


class mode():
	pass


if __name__ == '__main__':
	ci = ClassInterval(118,180,9)
	print(ci.class_interval())

	f = [3,5,9,12,5,4,2]
	x = [122,131,140,149,158,167,176]
	d1 = mean(f,x)
	print(d1.fx_finder())
	print(d1.get_mean())