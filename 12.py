from math import sqrt
from math import ceil

table = {}

def triangle():
	i, s = 2, 1
	while i:
		yield s+i, i
		s, i = s+i, i+1
		
def fac(num, f, cnt=0):
#	print num,
#	print ": ",
	while f > 0:
		if not num%f:
			if f in table:
				cnt += table[f]
#				print "%d is in table" % (f),
				break
			else:
#				print f,
				cnt += 1
		f -= 1
	if cnt:
		table[num] = cnt*2
#	print " => ",
#	print cnt*2
	return cnt*2

#n=3
#print fac(n, n)

max = 0

file = open("data.csv", 'w')

for i in triangle():
	num = fac(i[0], ceil(sqrt(i[0])))
	file.write("%d, %d\n" % (i[0], num))
	if num > max:
		print "New max is %3d (d = %2d) @ %10d" % (num, num - max, i[0])
		max = num
	if num > 500:
		print "Answer is: %d" % (i[0])
		break
