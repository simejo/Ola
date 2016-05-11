import data_utils

num_movie_scripts = 4
vocabulary_size = 200
path_for_file = 'X_train.txt'


"""
TODO: 
1. run generateEncodedFile on all the scripts
2. Remove the 
"""
def generateEncodedFile(filename, tokenized_sentences):
	f = open(filename, 'w')
	unk_id = dictionary['UNK']
	for sentence in tokenized_sentences:
		encoded_sentence = ""
		for word in sentence:
			if word in dictionary:
				encoded_word = dictionary[word]
			else:
				encoded_word = unk_id
			encoded_sentence += str(encoded_word) + " "
		encoded_sentence = encoded_sentence[:-1] # Remove final space
		f.write(encoded_sentence + '\n') # Write sentence to file
	f.close()


def createVocabulary(dictionary, vocabulary_path):
	f = open(vocabulary_path, 'w')
	for key in dictionary:
		f.write(dictionary[key] + '\n')
	f.close()



# Generate dictionary for dataset
print '------------------------------------------------'
print ' Generating dictionary based on ', str(num_movie_scripts - 1), ' scripts'
print '------------------------------------------------'

tokenized_data = data_utils.read_data(num_movie_scripts)
data, count, dictionary, reverse_dictionary = data_utils.build_dataset(tokenized_data, vocabulary_size)
createVocabulary(reverse_dictionary, 'vocabulary_for_3_movies.txt')

#DRIT I AA SLETT
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


# Generate a encoded file using the freated dictionary
print '------------------------------------------------'
print ' Creating encoded file using created dictionary'
print ' (Saved in  ', path_for_file, ')'
print '------------------------------------------------'
tokenized_sentences = data_utils.read_sentences(num_movie_scripts)
#print tokenized_sentences
generateEncodedFile(path_for_file, tokenized_sentences)






