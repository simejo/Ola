import data_utils

num_movie_scripts = 4
vocabulary_size = 200
path_for_file = 'X_train.txt'

def generateEncodedFile(filename, tokenized_sentences):
	f = open(filename, 'w')
	for sentence in tokenized_sentences:
		encoded_sentence = ""
		for word in sentence:
			if word in dictionary:
				encoded_word = dictionary[word]
			else:
				encoded_word = dictionary['UNK']
			encoded_sentence += str(encoded_word) + " "
		encoded_sentence = encoded_sentence[:-1] # Remove final space
		f.write(encoded_sentence + '\n') # Write sentence to file
	f.close()

# Generate dictionary for dataset
print '------------------------------------------------'
print ' Generating dictionary based on ', str(num_movie_scripts - 1), ' scripts'
print '------------------------------------------------'

tokenized_data = data_utils.read_data(num_movie_scripts)
data, count, dictionary, reverse_dictionary = data_utils.build_dataset(tokenized_data, vocabulary_size)

""" DRIT I AA SLETT
print '-------- data'
print data
print '-------- count'
print count
print '-------- dictionary'
data_utils.print_dic(dictionary, 5)
print dictionary
print '-------- reverse_dictionary'
data_utils.print_dic(reverse_dictionary, 5)
print reverse_dictionary
"""
print '------------------------------------------------'
print ' Creating encoded file using created dictionary'
print ' (Saved in  ', path_for_file, ')'
print '------------------------------------------------'
tokenized_sentences = data_utils.read_sentences(num_movie_scripts)
generateEncodedFile(path_for_file, tokenized_sentences)





