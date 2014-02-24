import time
import sys
import random
import os

def main():

	os.system('clear') #clears the UNIX terminal for the ultimate typing experience

	text_source = open('google-10000-english.txt', 'r+');
	words = []
	user_input = []
	count = 10
	lines = text_source.readlines()
	
	for x in range(1, 300):
		words.append(random.choice(lines).replace('\n', ''))

	initialTime = time.time()

	#60 second typing test
	while((time.time() - initialTime) < 60):

		for word in words[count-9:count]:
			print word,

		print '\n\n'
		print 'TYPE THE ABOVE WORDS'
		print '--------------------'

		user_input.append(raw_input())
		os.system('clear')

		count += 10

	#calculating score


	

if __name__ == '__main__':
	main()
