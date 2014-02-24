import time
import sys
import random
import os

def get_net_WPM(input_keystrokes, errors, time_elapsed):
	result = input_keystrokes/5
	result = result - errors
	result = result/time_elapsed
	return result

def check_time(initial, current):
	return current - initial

def main():

	os.system('clear') #clears the UNIX terminal for the ultimate typing experience

	time_elapsed = 0.0

	keystrokes = 0
	text_source = open('google-10000-english.txt', 'r+');
	words = []
	user_input = []
	count = 10
	errors = 0
	lines = text_source.readlines()
	
	for x in range(1, 300):
		words.append(random.choice(lines).replace('\n', ''))

	initialTime = time.time()

	#60 second typing test
	while((time.time() - initialTime) < 60):

		for word in words[count-10:count]:
			print word,

		print '\n\n'
		print 'TYPE THE ABOVE WORDS'
		print '--------------------'

		user_input.append(raw_input())
		time_elapsed = -(check_time(time.time(), initialTime))
		
		os.system('clear')

		count += 10

	count = 0
	#calculating score
	for word_set in user_input:
		word_set = word_set.split(' ')
		
		for word in word_set:
			keystrokes += len(word)
			if word != words[count]:
				errors += 1

			count += 1

	#os.system('clear')
	print "YOUR TYPING SPEED IS: " + str(int(get_net_WPM(keystrokes, errors, (time_elapsed/60))))
	print "YOU TYPED " + str(errors) + " WRONG WORDS!" 


	

if __name__ == '__main__':
	main()
