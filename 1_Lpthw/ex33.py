# -- coding: utf-8 --
number = []

def loop(end, step):
	for i in range(end):
	    print "At the top i is %d" %i
	    number.append(i)
	     
	    i += step
	    print "Number now:", number
	    print "At the bottom i is %d" %i

loop(8, 2)
print "The number:"

for num in number:
    print num
