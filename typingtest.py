import time
import sys
import random
import os

def main():

	os.system('clear') #clears the UNIX terminal for the ultimate typing experience

	text_source = open('google-10000-english.txt', 'r+');
	words = []
	lines = text_source.readlines()

	initialTime = time.time()

	#60 second typing test
	while ((time.time() - initialTime) < 60):
		
		#for x in range (0, 10):
		#	print(random.choice(lines).replace('\n', '')),
		#print "\n\n"

	

if __name__ == '__main__':
	main()
