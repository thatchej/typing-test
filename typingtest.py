import time
import sys
import random
import os

def main():

	os.system('clear') #clears the UNIX terminal for the ultimate typing experience

	text_source = open('google-10000-english.txt', 'r+');
	words = []
	lines = text_source.readlines()
	for x in range(1, 300):
		words.append(random.choice(lines).replace('\n', ''))

	initialTime = time.time()

	#60 second typing test

		
	for word in words[:10]:
		print word,
		READ IN INPUT
		STORE INPUT WORDS IN ARRAY

		os.system('clear')

		if (time.time() - initialTime) < 60))	
			break

	

if __name__ == '__main__':
	main()
