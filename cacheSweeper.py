# Authors: Stephen De L'Iorio and Andrew Ivarson
# Date: June 2015
#
# This is our final project for CSc 483 - Advanced Hardware, where we
# try to implement a fun game.

def cache(block, line):
	bl = []
	for x in range (0, block):
		bl.append(1)

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

def printCacheMem(cch, mem, memSize, line, block):
	index = 0
	toRet = ""
	for x in range (0, memSize):
		index = index + 1
	return

size = 64
simon = memory(size)
block = 4
line = 4
drew = cache(block, line)
print "Memory:"
print simon
print "Cache:"
printCache(drew)
print "CacheMem:"
printCacheMem(drew, simon, size, line, block)
