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
size = 256 # how big memory can be

keyphrase = ""
solvephrase = ""

keywords4 = ["john", "fish", "goat", "jump", "meat"]
keywords5 =	["sword", "preach", "gospel", "sonic"]

phrase1 = "caches are kinda cool"
phrase14 = ["hjhdas jra gelnj hmmi","sfsdar fqa jemhf snnk",\
			"agaebr gqb ifltg ammj","mjmdar jqa gekpj mllh","amafbr mqb igltm annj"]
phrase15 = ["osocdp snd gejrs okkh","epedcs pqc iflap emmj",\
			"sgsber gqe fcjpg skkh","nsndcr sqc gekis nllh"]

# returns hex representation of the character inputed
def charToHexAscii(theChar):
	return hex(ord(theChar))

# given a string, prints each individual character in hex
def testCharToHex(theWord):
	 for x in range (0, len(theWord)):
	 	print charToHexAscii(theWord[x])
	 return

def fillMem(lines, block):
	toRet = []
	word = ""
	
	global solvephrase
	if lines > 4 :
		randIndex = random.randint(0,3)
		word = keywords4[randIndex]
		solvephrase = phrase14[randIndex]
	else :
		randIndex = random.randint(0,4)
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
	print toRet
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
			else :
				print "Nope!"
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

def printSolvePhrase():
	print solvephrase
	return

# Given the number of lines and blocks in a cahce, creates a dictionary
# in which each key refers to a line of cache, and each line is a list
# of size num_Blocks
def makeKeys(lines, num_Blocks):
	toRet = {}
	itera = 0
	while (itera < lines):
		toRet[itera] = []
		itera += num_Blocks

	return toRet

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
	print "Here, you are given a phrase to decrypt. It is encrypted using a Caesar Cipher."
	print "Through pulling data from memory into cache, you should find the keyword used to"
	print "decrypt the message."
	print "Here is your message. Good luck, soldier."
	allMem = memory(size)
	block = random.randint(1, 8)
	while not (block != 0 and ((block & (block - 1) == 0))):
		block = random.randint(1, 8)
	line = random.randint(4, size/block)
	# make sure # of lines is a power of 2
	while not (line != 0 and ((line & (line - 1) == 0))):
		line = random.randint(4, size/block)
	# block = 1
	# line = 16
	theCache = cache(block, line)
	drew = fillMem(line, block)
	print block
	print line
	global keyphrase
	keyphrase = phrase1
	# print solvephrase
	print userInput()
	print int(userInput(),hexBase)
	print convertHex(userInput())
	print convertBin(userInput())

	

	# print "Memory:"
	# print allMem
	# print "Cache:"
	# printCache(theCache)
	# print "CacheMem:"
	# printCacheMem(theCache, allMem, size, line, block)

main()