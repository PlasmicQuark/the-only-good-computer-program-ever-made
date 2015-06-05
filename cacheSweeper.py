# Authors: Stephen De L'Iorio and Andrew Ivarson
# Date: June 2015
#
# This is our final project for CSc 483 - Advanced Hardware, where we
# try to implement a fun game.

import random
import re
regex = r"""^0x([0-9]|[a-f]){2}$"""
inputRegex = re.compile(regex)

def userInput():
	notValid = True
	while notValid:
		address = raw_input("Provide a memory address to access of the form '0x_ _': ")
		address.lower()
		if inputRegex.match(address):
			notValid = False
		else:
			print "Provided memory address is not valid. Try again."

	return address

def convertBin(binString):
	return bin(int('1'+parts[1],16))[3:]

def convertHex(hexString):
	return int(hexString,16)

def main():
	print "Welcome to CacheSweeper."

	print userInput()
	print int(userInput(),16)
	print int(userInput(),2)

main()

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
block = random.randint(1, 8)
line = random.randint(1, size/block)
drew = cache(block, line)
print "Memory:"
print simon
print "Cache:"
printCache(drew)
print "CacheMem:"
printCacheMem(drew, simon, size, line, block)
