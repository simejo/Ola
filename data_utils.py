import numpy as np
import math

num_movie_scripts = 3

def getDataSets(num_movie_scripts):
	X_train = []
	y_train = []
	for i in range(1, num_movie_scripts):
		path = 'data/'+str(i)+'raw.txt'
		f = open(path, 'r')
		print 'Reading ', path, '...'
		
		lines = [line.rstrip('\n') for line in open(path)]
		X_train_temp = []
		y_train_temp = []
		for line in lines:
			X_train_temp.append(line)
			y_train_temp.append(line)
		X_train_temp.pop()
		y_train_temp.pop(0)

		X_train.extend(X_train_temp)
		y_train.extend(y_train_temp)
		f.close()

	X_train = np.array(X_train)
	y_train = np.array(y_train)

	# Use 1/10 as development data
	print len(X_train)
	num_dev_data = math.floor(len(X_train)/10)
	num_train_data = len(X_train)-num_dev_data
	X_dev = X_train[num_train_data:]
	y_dev = y_train[num_train_data:]
	X_train = X_train[:num_train_data]
	y_train = y_train[:num_train_data]
	#print len(X_train), len(y_train), len(X_dev), len(y_dev)

	# Tokenize all the datasets - do it before?


	return X_train, y_train, X_dev, y_dev


def checkDataSets(X_train, y_train, X_dev, y_dev, num_iters):
	for i in range(0,num_iters):
		print '--------------------------'
		print 'User: 	:',X_train[i]
		print 'Ola:	:', y_train[i]


def basic_tokenizer(sentence):
  """Very basic tokenizer: split the sentence into a list of tokens."""
  words = []
  for space_separated_fragment in sentence.strip().split():
    words.extend(re.split(_WORD_SPLIT, space_separated_fragment))
  return [w for w in words if w]


X_train, y_train, X_dev, y_dev = getDataSets(num_movie_scripts)

#checkDataSets(X_train, y_train, 0,0,10)