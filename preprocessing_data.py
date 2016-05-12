import re
import collections
import shutil

num_movie_scripts = 100
vocabulary_size = 2000
fraction_dev = 50
path_for_x_train = 'X_train.txt'
path_for_y_train = 'y_train.txt'
path_for_x_dev = 'X_dev.txt'
path_for_y_dev = 'y_dev.txt'


_PAD = b"_PAD"
_GO = b"_GO"
_EOS = b"_EOS"
_UNK = b"_UNK"
_START_VOCAB = [_PAD, _GO, _EOS, _UNK]

PAD_ID = 0
GO_ID = 1
EOS_ID = 2
UNK_ID = 3


"""
TODO: 
1. run generateEncodedFile on all the scripts
2. Remove the space after the 'fnutts' (I' ll, haven' t)
"""

#FROM DATA UTILS
# Build the dictionary with word-IDs from self-made dictionary and replace rare words with UNK token.
def build_dataset(words, vocabulary_size):
	count = [['_UNK', -1]]
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

def createVocabulary(dictionary, vocabulary_path):
	f = open(vocabulary_path, 'w')
	
	for key in dictionary:
		f.write(dictionary[key] + '\n')
	f.close()


def generateEncodedFile(x_train_file, y_train_file, x_dev_file, y_dev_file, tokenized_sentences, dictionary):
	encoded_holder = []
	f1 = open(x_train_file, 'w')

	last_line = tokenized_sentences.pop()
	first_line = tokenized_sentences.pop(0)
	dev_counter = int(len(tokenized_sentences) - len(tokenized_sentences)/fraction_dev)

	unk_id = dictionary['_UNK']
	first_line_encoded = encode_sentence(first_line, dictionary, unk_id)
	f1.write(first_line_encoded + '\n')

	# Creates data for X_train
	for x in xrange(dev_counter):
		encoded_sentence = encode_sentence(tokenized_sentences[x], dictionary, unk_id)
		encoded_holder.append(encoded_sentence)
		f1.write(encoded_sentence + '\n') # Write sentence to file
	f1.close()

	d1 = open(x_dev_file, 'w')
	# Creates data for x_dev_file
	for x in xrange(dev_counter, len(tokenized_sentences)):
		encoded_sentence = encode_sentence(tokenized_sentences[x], dictionary, unk_id)
		encoded_holder.append(encoded_sentence)
		d1.write(encoded_sentence + '\n') # Write sentence to file

	d1.close()

	# Creates data for y_train
	f2 = open(y_train_file, 'w')

	for x in xrange(dev_counter + 1):
		f2.write(encoded_holder[x] + '\n') # Write sentence to file

	f2.close()

	# Creates data for y_dev
	d2 = open(y_dev_file, 'w')
	for x in xrange(dev_counter + 1, len(tokenized_sentences)):
		d2.write(encoded_holder[x] + '\n') # Write sentence to file

	last_line_encoded = encode_sentence(last_line, dictionary, unk_id)
	d2.write(last_line_encoded + '\n')
	d2.close()
	
def encode_sentence(sentence, dictionary, unk_id):
	# Extract first word
	if not sentence:
		return ""
	first_word = sentence.pop(0)
	if first_word in dictionary:
		encoded_sentence = str(dictionary[first_word])
	else:
		encoded_sentence = str(unk_id)

	# Loop rest of the words
	for word in sentence:
		if word in dictionary:
			encoded_word = dictionary[word]
		else:
			encoded_word = unk_id
		encoded_sentence += " " + str(encoded_word)
	return encoded_sentence




# Generate dictionary for dataset
print '------------------------------------------------'
print ' Generating dictionary based on ', str(num_movie_scripts - 1), ' scripts'
print '------------------------------------------------'


#FROM DATA UTILS
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
			data_tokens_temp.extend(re.findall(r'\S+', line))
		data_tokens.extend(data_tokens_temp)

	return data_tokens




tokenized_data = read_data(num_movie_scripts)
data, count, dictionary, reverse_dictionary = build_dataset(tokenized_data, vocabulary_size)
createVocabulary(reverse_dictionary, 'vocabulary_for_' + str(num_movie_scripts) + '_movies.txt')


# Generate a encoded file using the freated dictionary
print '------------------------------------------------'
print ' Creating encoded file using created dictionary'
print ' (Saved in  ', path_for_x_train, ')'
print '------------------------------------------------'

# FROM DATA UTILS
# Reads data and puts every sentence in a TWO DIMENSIONAL array as tokens
# data_tokens[0] = ['This', 'is', 'a', 'sentence']
def read_sentences(num_movie_scripts):
	data_tokens = []
	# Append each line in file to the set
	for i in range(1, num_movie_scripts):
		path = 'data/'+str(i)+'raw.txt'
		print 'Reading ', path, '...'
		lines = [line.rstrip('\n') for line in open(path)]
		data_tokens_temp = []
		for line in lines:
			# Tokenize each sentence
			data_tokens_temp.append(re.findall(r'\S+', line))
		data_tokens.extend(data_tokens_temp)
	return data_tokens

tokenized_sentences = read_sentences(num_movie_scripts)
#print tokenized_sentences
generateEncodedFile(path_for_x_train, path_for_y_train, path_for_x_dev, path_for_y_dev, tokenized_sentences, dictionary)




#-----------------------Printing methods----------------------------
def print_dic(dic, counter):
	c = 0
	for x in dic:
		print x
		c += 1
		if(c == counter):
			break

def print_info(data, count, dictionary, reverse_dictionary):
	print '-------- data'
	print data
	print '-------- count'
	print count
	print '-------- dictionary'
	print_dic(dictionary, 5)
	print dictionary
	print '-------- reverse_dictionary'
	print_dic(reverse_dictionary, 5)
	print reverse_dictionary

