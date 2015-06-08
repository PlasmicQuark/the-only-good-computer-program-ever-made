# Authors: Stephen DIorio and Andrew Ivarson
# Date: June 2015
#
# This is our final project for CSc 483 - Advanced Hardware, where we
# try to implement a fun game.

import random
import re
import math
import time
import sys

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
tagIndex = 0 # the index in the cache for the tag
validBitIndex = 1 # the index in the cache for the valid bit
dataIndex = 2 # the index in the cache leading to the list of data



keyphrase = ""
solvephrase = ""

keywords4 = ["john", "fish", "goat", "jump", "meat"]
keywords5 =	["sword", "preach", "gospel", "sonic"]

phrase1 = "caches are kinda cool"
phrase14 = ["hjhdas jra gelnj hmmi","sfsdar fqa jemhf snnk",\
			"agaebr gqb ifltg ammj","mjmdar jqa gekpj mllh","amafbr mqb igltm annj"]
phrase15 = ["osocdp snd gejrs okkh","epedcs pqc iflap emmj",\
			"sgsber gqe fcjpg skkh","nsndcr sqc gekis nllh"]

# Returns hex representation of the character inputed
def charToHexAscii(theChar):
	return hex(ord(theChar))

# Given a string, prints each individual character in hex
def testCharToHex(theWord):
	for x in range (0, len(theWord)):
		print charToHexAscii(theWord[x])
	return

def fillMem(lines, block):
	toRet = []
	word = ""

	global solvephrase
	if lines > 4 :
		randIndex = random.randint(0,4)
		word = keywords4[randIndex]
		solvephrase = phrase14[randIndex]
	else :
		randIndex = random.randint(0,3)
		word = keywords5[randIndex]
		solvephrase = phrase15[randIndex]


	print solvephrase

	wordIter = 0
	activate_Word_Insert = False
	blockIter = 0
	start = 0
	current = 0
	for x in range (0, size):
		randomFiller = random.randint(91, 157)
		filler = 0
		if x % lines == 0 :
			activate_Word_Insert = True
			start = x
			current = x
		# if we are currently inserting the word
		if (activate_Word_Insert == True) and (blockIter < block*len(word)) and current == x:
			filler = word[wordIter]
			wordIter += 1
			blockIter += block
			current = x + block
		# otherwise reset all of the adding stuff
		elif (blockIter >= block*len(word)):
			blockIter = 0
			wordIter = 0
			activate_Word_Insert = False
			current = 0
			start = 0
		if filler == 0 :
			toRet.append(hex(randomFiller))
		else :
			toRet.append(filler)
	# print toRet
	return toRet

# Designed to take in user input, make sure it is a valid memory address,
# and return the address they provided to be used later.
def userInput():
	notValid = True
	while notValid:
		inputString = "Privode a memory address to access of the form '0x_ _'\nYou may also enter solve to solve the puzzle: "
		address = raw_input(inputString)
		address.lower()
		if inputRegex.match(address):
			notValid = False
		elif (address == "solve"):
			solution = raw_input("Enter in your solution: ")
			solution.lower()
			# print solution
			#print keyphrase
			if (solution == keyphrase):
				print "You did it!"
				sys.exit()
			else :
				print "Nope!"
		else:
			print "Provided memory address is not valid. Try again."
	if (address == -1):
		return address
	else :
		return convertHexToBin(address)

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
	return int(hexString,hexBase)

# Given a binary string, converts that into its
# base 10 integer equivalent.
def convertBinToInt(binString):
	if (binString == ''):
		return 0
	else:
		return int(binString, binBase)

# Prints the phrase that solves the problem.
def printSolvePhrase():
	print solvephrase
	return

# Given the number of lines and blocks in a cache, creates a dictionary
# in which each key refers to which set of cache, and each line is a list
# containing in the 0th index the tag, in the 1st index the valid bit, and
# in the 2nd index a list containing all of the blocks of data.
def cache(lines, num_Blocks):
	toRet = {}
	itera = 0
	for x in range (0,lines):
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

# Adds the provided data to the appropriate spot in cache based on
# its memory address.
def addToCache(tag, index, blockOff, newData, theCache):
	numTag = convertBinToInt(tag)
	numIndex = convertBinToInt(index)
	numBlock = convertBinToInt(blockOff)
	theCache[numIndex][validBitIndex] = 1
	theCache[numIndex][tagIndex] = numTag
	theCache[numIndex][dataIndex][numBlock] = newData

	return theCache

# Grabs out of memory the data stored at the provided address and returns it.
def getData(mem, addr):
	return mem[convertBinToInt(addr)]

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

	print "Here, you are given a phrase to decrypt. It is encrypted using a Caesar Cipher."
	print "Through pulling data from memory into cache, you should find the keyword used to"
	print "decrypt the message."
	print "Here is your message. Good luck, soldier."
	block = random.randint(1, 8)
	while not (block != 0 and ((block & (block - 1) == 0))):
		block = random.randint(1, 8)
	line = random.randint(4, size/block)
	# make sure # of lines is a power of 2
	while not (line != 0 and ((line & (line - 1) == 0))):
		line = random.randint(4, size/block)

	allMem = fillMem(line, block)

	global keyphrase
	keyphrase = phrase1

	setSize = math.log(line, binBase)
	blockOffSize = math.log(block, binBase)
	tagSize = (addressSize*hexIntConv) - setSize - blockOffSize
	theCache = cache(line, block)
	print line
	print block
	while True:
		useIn = userInput()
		tag = getTag(useIn, tagSize)
		index = getIndex(useIn, setSize, tagSize)
		blockOff = getBlockOffset(useIn, setSize, tagSize)
		if not inCache(tag, index, theCache):
			print "Item not found in cache; fetching it from memory. Please wait."
			data = getData(allMem, useIn)
			# time.sleep(10) # 10 sec penalty for accessing memory out of cache
			theCache = addToCache(tag, index, blockOff, data, theCache)
			print "Cache: "
			print theCache

	return

main()