import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# import files
hg360 = pd.read_csv('HG360_UI_copy.csv')
command_center = pd.read_csv('command_center_2021.csv')

# make HG360 client name into list
name_list360 = hg360['Name'].to_list()

# make command center Client names a list and remove duplicates
name_list_command_center = command_center['Client'].to_list()
#name_list_command_center = list(set(command_center['Client'].to_list()))

# empty list to store matches
mat1 = []
threshold = 82

# iterating through name_list_command_center to extract 
# it's closest match from Hg360
for i in name_list_command_center:
    mat1.append(process.extract(i, name_list360, limit=1))

# find the closest match based on threshold
# create list
result = []
for j in mat1:
    for k in j:
        if k[1] > threshold:
            result.append(k[0])
        else:
            result.append('none')
result     
    


#len(name_list_command_center)

command_center['matches'] = result

command_center.head(25)

# merge command_center with hg360

merged_customers = command_center.merge(hg360, how='inner', left_on='matches', right_on='Name')

# export csv
# maybe it worked?
merged_customers.to_csv('merged_customer_data_maybe.csv')
