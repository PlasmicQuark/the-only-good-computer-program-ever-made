# Authors: Stephen DIorio and Andrew Ivarson
# Date: June 2015
#
# This is our final project for CSc 483 - Advanced Hardware, where we
# try to implement a fun game.

import random
import re
import math

# Regular expression statements for validating user input.
regex = r"""^0x([0-9]|[a-f]){2}$"""
inputRegex = re.compile(regex)
# Global constants
hexBase = 16
binBase = 2
addressOffset = 2 # the '0x' the leads every hex memory address
size = 64 # how big memory can be

# Designed to take in user input, make sure it is a valid memory address,
# and return the address they provided to be used later.
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

# Converts a hex string of the form '0x_ _' and transforms it into its
# binary string representation.
def convertBin(binString):
	return bin(int(binString,hexBase))[addressOffset:].zfill(len(binString[addressOffset:])*int(math.log(hexBase,binBase)))

# Given a string representing a hexadecimal number, converts it to its
# base 10 integer equivalent.
def convertHex(hexString):
	return int(hexString, hexBase)

# Generates a cache with each line having the number of blocks provided.
def cache(block, line):
	bl = []
	for x in range (0, block):
		bl.append(1)

	ca = []
	for x in range (0, line):
		ca.append(bl)
	return ca

# Generates an empty data memory of the specified size.
def memory(size):
	mem = []
	for x in range (0, size):
		mem.append(0)
	return mem

# Prints the contents of the cache.
def printCache(cch):
	print '\n'.join(map(str, cch))
	return

def printCacheMem(cch, mem, memSize, line, block):
	index = 0
	toRet = ""
	for x in range (0, memSize):
		index = index + 1
	return

def main():
	print "Welcome to CacheSweeper."

	print userInput()
	print int(userInput(),hexBase)
	print convertHex(userInput())
	print convertBin(userInput())

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

main()