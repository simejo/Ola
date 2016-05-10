import numpy as np
import math
import re
import collections


# Regular expressions used to tokenize.
_WORD_SPLIT = re.compile(b"([.,!?\"':;)(])")
_DIGIT_RE = re.compile(br"\d")




num_movie_scripts = 3
#vocabulary_size = 200

# Reads data and puts every sentence in arrays as tokens
def read_data(num_movie_scripts):
	data_tokens = []
	# Append each line in file to the set
	for i in range(1, num_movie_scripts):
		path = 'data/'+str(i)+'raw.txt'
		print 'Reading ', path, '...'
		lines = [line.rstrip('\n') for line in open(path)]
		data_tokens_temp = []
		for line in lines:
			# Tokenize each sentence
			data_tokens_temp.extend(re.split(_WORD_SPLIT, line))
		data_tokens.extend(data_tokens_temp)
	return data_tokens

# Build the dictionary with word-IDs from self-made dictionary and replace rare words with UNK token.
def build_dataset(words, vocabulary_size):
	count = [['UNK', -1]]
	print 'words************'
	print words[:5]
	count.extend(collections.Counter(words).most_common(vocabulary_size - 1))
	dictionary = dict()
	for word, _ in count:
		dictionary[word] = len(dictionary)
	data = list()
	unk_count = 0
	for word in words:
		if word in dictionary:
			index = dictionary[word]
		else:
			index = 0  # dictionary['UNK']
			unk_count = unk_count + 1
		data.append(index)
	count[0][1] = unk_count
	reverse_dictionary = dict(zip(dictionary.values(), dictionary.keys()))
	return data, count, dictionary, reverse_dictionary

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


words = read_data(3)
#data, count, dictionary, reverse_dictionary = build_dataset(words,)

def print_dic(dic, counter):
	c = 0
	for x in dic:
		print x
		c += 1
		if(c == counter):
			break





#checkDataSets(X_train, y_train, 0,0,10)


