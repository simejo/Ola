import fileinput

def read_data(num_movie_scripts):
	data_tokens = []
	# Append each line in file to the set
	for i in range(1, num_movie_scripts):
		path = 'data/'+str(i)+'raw.txt'
		raw = open(path,'r+')
		print 'Reading ', path, '...'
		holder = ""
		for line in raw:
			this_line = line
			if "' il" in this_line:
				this_line = this_line.replace("' il", "'ll")
			if "' " in line:
				this_line = this_line.replace("' ","'")
			if " ?" in line:
				this_line = this_line.replace(" ?", "?")
			holder += this_line
		raw.seek(0)
		raw.write(holder)
		raw.truncate()
		raw.close()


read_data(2318)