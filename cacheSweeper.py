# Authors: Stephen DIorio and Andrew Ivarson
# Date: June 2015
#
# This is our final project for CSc 483 - Advanced Hardware, where we
# try to implement a fun game.

import random
import re
import math
import time

# Regular expression statements for validating user input.
regex = r"""^0x([0-9]|[a-f]){2}$"""
inputRegex = re.compile(regex)
# Global constants
hexBase = 16
binBase = 2
addressOffset = 2 # the '0x' the leads every hex memory address
size = 256 # how big memory can be
addressSize = 2 # the number of hex digits the user will put in
hexIntConv = 4 # how many bits are stored within 1 hex digit
tagIndex = 0
validBitIndex = 1
dataIndex = 3

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
def convertHexToBin(hexString):
	return bin(int(hexString,hexBase))[addressOffset:].zfill(addressSize*int(math.log(hexBase,binBase)))

# Converts an integer to its binary string representation.
def convertIntToBin(num):
	return bin(num)[addressOffset:].zfill(addressSize*int(math.log(hexBase,binBase)))

# Given a string representing a hexadecimal number, converts it to its
# base 10 integer equivalent.
def convertHexToInt(hexString):
	return int(hexString, hexBase)

# Given a string representing a binary number, converts it to its
# base 10 integer equivalent.
def convertBinToInt(binString):
	return int(binString, binBase)

# Given the number of lines and blocks in a cache, creates a dictionary
# in which each key refers to which set of cache, and each line is a list
# of size num_Blocks
def cache(lines, num_Blocks):
	toRet = {}
	itera = 0
	for x in range (0,lines/num_Blocks):
		toRet[x] = [-1,0]+[[-1]*num_Blocks]

	return toRet

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

# Checks to see if an item in memory is currently in the cache. This looks at
# the provided set and checks to see if the data is valid and if the
# tag matches the address the user is asking for.
def inCache(tag, index, theCache):
	toRet = False
	numTag = convertBinToInt(tag)
	numIndex = convertBinToInt(index)

	if theCache[numIndex][validBitIndex] and theCache[numIndex][tagIndex] == numTag:
		toRet = True

	return toRet

def addToCache(tag, index, blockOff, newData, theCache):
	numTag = convertBinToInt(tag)
	numIndex = convertBinToInt(index)
	numBlock = convertBinToInt(blockOff)

	theCache[numIndex][validBitIndex] = 1
	theCache[numIndex][tagIndex] = numTag
	theCache[numIndex][dataIndex][numBlock] = newData

	return theCache

# Given a memory address and the size of the tag, gets the portion of the
# address corresponding to the tag
def getTag(address, tagSize):
	return address[:int(tagSize)]

# Given a memory address and the size of the tag and the number of sets,
# gets the portion of the address corresponding to the index
def getIndex(address, setSize, tagSize):
	return address[int(tagSize):int(tagSize+setSize)]

# Given a memory address and the size of the tag and the number of sets,
# gets the portion of the address corresponding to the block offset
def getBlockOffset(address, setSize, tagSize):
	return address[int(tagSize+setSize):]

def main():
	print "Welcome to CacheSweeper."

	# print userInput()
	# print int(userInput(),hexBase)
	# print convertHexToBin(userInput())
	# print convertBin(userInput())
	# print convertIntToBin(input())

	allMem = memory(size)
	# block = random.randint(1, 8)
	# line = random.randint(4, size/block)
	block = 2
	line = 16
	setSize = math.log(line, binBase)
	blockOffSize = math.log(block, binBase)
	tagSize = (addressSize*hexIntConv) - setSize - blockOffSize
	theCache = cache(line, block)
	# print theCache
	# return

	# add = '12345678'
	# print getTag(add, tagSize)
	# print getIndex(add, setSize, tagSize)
	# print getBlockOffset(add, setSize, tagSize)
	# return

	while True:
		useIn = userInput()
		tag = getTag(useIn, tagSize)
		index = getIndex(useIn, setSize, tagSize)
		blockOff = getBlockOffset(useIn, setSize, tagSize)
		if not inCache(tag, index, blockOff, theCache):
			print "Item not found in cache; fetching it from memory. Please wait."
			data = getData()
			time.sleep(10) # 10 sec penalty for accessing memory out of cache
			theCache = addToCache(tag, index, blockOff, data, theCache)

	print "Memory:"
	print allMem
	print "Cache:"
	print theCache.keys()
	# printCache(theCache)
	# print "CacheMem:"
	# printCacheMem(theCache, allMem, size, line, block)

main()