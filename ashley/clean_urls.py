import csv
import pandas as pd

# get input and output file names
input_file_name = input('\n Input file name (must end with .csv): ')
output_file_name = input('\n Output file name (must end with .csv): ')

# read in the input file
csv_file = open(input_file_name)
csv_reader = csv.reader(csv_file)

# initialize data structures
original_url_array = []
original_url_and_cleaned_url_dictionary = {}

# append csv rows to an array
for row in csv_reader:
	original_url_array.append(row[0])

original_url_array.pop(0) # remove the first value from the array (the csv's header)

# strip and prefix urls
def clean_url(url):

	# strip url of certain characters to normalize it
	# remove variations of 'http' and 'https' anywhere these strings occur in the url
	cleaned_url = url.replace('https://www.', '').replace('https://', '').replace('http://www.', '').replace('http://', '')
	# remove prefixed 'www.' from the url
	if cleaned_url[0:4] == 'www.':
		cleaned_url = cleaned_url[4:len(cleaned_url)]
	# remove trailing double slashes from the url
	if cleaned_url[-2:] == '//':
		cleaned_url = cleaned_url[0:-2]
	# remove trailing slash from the url
	if cleaned_url[-1:] == '/':
		cleaned_url = cleaned_url[0:-1]
	# remove all characters after the first slash
	cleaned_url = cleaned_url.split('/', 1)[0]

	return(cleaned_url)

counter = 1

# get response url, clean it, and add it to the dictionary
for original_url in original_url_array:

	cleaned_url = clean_url(original_url)

	# add url, input url and response url to dictionaries
	original_url_and_cleaned_url_dictionary[original_url] = cleaned_url

	print(counter)
	counter = counter + 1

# convert dictionaries to data frames
original_url_and_cleaned_url_data_frame = pd.DataFrame(original_url_and_cleaned_url_dictionary.items())
original_url_and_cleaned_url_data_frame.columns = ['original_url', 'cleaned_url'] # add column names to the data frame

# export data as a .csv
original_url_and_cleaned_url_data_frame.to_csv(output_file_name, index = False)

print()
