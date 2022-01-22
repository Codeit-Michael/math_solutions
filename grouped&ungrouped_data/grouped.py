from prettytable import PrettyTable

# for grouped data
class ClassInterval():

	def __init__(self,lowest:int,highest:int,class_size:int):
		self.lowest = lowest
		self.highest = highest+1
		self.class_size = class_size
		self.single_class = []

		self.numlist_move = 0
		for x in range(self.lowest,self.highest,self.class_size):
			self.single_class.append([])
			for y in range(x,x+self.class_size):
					self.single_class[self.numlist_move].append(y)
			self.numlist_move += 1


	def class_interval_table(self):
		CI_table = PrettyTable(['class interval'])
		for x in range(len(self.single_class)):
			CI_table.add_row([f'{self.single_class[x][0]} - {self.single_class[x][-1]}'])
		return CI_table



class mean(ClassInterval):
	# total_fx = '∑𝑓𝑋'
	# N = '𝑁'

	def __init__(self,f:list,x:list):
		self.f = f
		self.x = x
		self.fx = []


	def _fx_finder(self):
		for i in range(0,len(self.f)):
			new = (self.f[i] * self.x[i])
			self.fx.append(new)
		return self.fx


	def _mean_solution(self,Efx,n,total):
		meantable = PrettyTable(['mean'])
		meantable.add_row(['Efx/N\n'])
		meantable.add_row([f'{Efx}\n---\n{n}\n'])
		meantable.add_row([f'= {total}'])
		return meantable


	def get_mean(self):
		self._fx_finder()
		total_fx = sum(self.fx)
		N = sum(self.f)
		mean_answer = total_fx/N
		return self._mean_solution(total_fx,N,mean_answer)



class median(ClassInterval):
	# cumf = </> cum f
	# N = N/2
	# fmBefore = ∑𝑓𝑋-1

	def __init__(self,f:list,cumf:list,lowest:int,highest:int,class_size:int):
		self.f = f
		self.cumf = cumf
		super().__init__(lowest,highest,class_size)


	def _median_solution(self,N,fmBefore,Lm,fm,i,total_median):
		mediantable = PrettyTable(['median'])
		mediantable.add_row(['((N/2) - Efx-1)\nLm + ---------------- i\nfm\n'])
		mediantable.add_row([f'(({N*2}/2) - {fmBefore})\n{Lm} + --------------- {i}\n{fm}\n'])
		mediantable.add_row([f'({N} - {fmBefore})\n{Lm} + --------------- {i}\n{fm}\n'])
		mediantable.add_row([f'({N - fmBefore})\n{Lm} + --------------- {i}\n{fm}\n'])
		mediantable.add_row([f'{Lm} + ({(N-fmBefore)/fm}) {i}\n'])
		mediantable.add_row([f'{Lm} + {((N-fmBefore)/fm)*i}\n= {total_median}'])
		return mediantable


	def get_median(self):
		N = self.cumf[-1]//2
		for x in cumf:
			if N >= x:
				fmBefore = x
		midclass = self.single_class[self.cumf.index(fmBefore)+1]
		Lm = midclass[0]
		fm = self.f[self.cumf.index(fmBefore)+1]
		i = midclass[-1] - midclass[0] + 1

		mid = (N-fmBefore)/fm * i
		total_median = Lm + mid
		
		return self._median_solution(N,fmBefore,Lm,fm,i,total_median)



class mode(ClassInterval):
	pass



if __name__ == '__main__':
	ci = ClassInterval(118,180,9)
	f = [3,5,9,12,5,4,2]
	x = [122,131,140,149,158,167,176]
	cumf = [3,8,17,29,34,38,40]

	my_mean = mean(f,x)
	print(my_mean.get_mean())

	my_median = median(f,cumf,118,180,9)
	# print(my_median.class_interval_table())
	print(my_median.get_median())