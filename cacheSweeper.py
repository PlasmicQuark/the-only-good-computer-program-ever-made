# Authors: Stephen De L'Iorio and Andrew Ivarson
# Date: June 2015
#
# This is our final project for CSc 483 - Advanced Hardware, where we
# try to implement a fun game.

def cache(block, line):
	bl = []
	for x in range (0, block):
		bl.append(0)

	ca = []
	for x in range (0, line):
		ca.append(bl)
	return ca

def memory(size):
	mem = []
	for x in range (0, size):
		mem.append(0)
	return mem

def printCache(cch):
	print '\n'.join(map(str, cch))
	return

size = 256
simon = memory(size)
block = 8
line = 32
drew = cache(block, line)
print "Memory:"
print simon
print "Cache:"
printCache(drew)

