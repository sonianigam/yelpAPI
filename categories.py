import json
import sys
import itertools

categories = []

#read and load data from infile
response = open(sys.argv[1])
decoded_response = response.read()
jsonResponse=json.loads(decoded_response)

#populate list
jsonData = jsonResponse
for item in jsonData:
    name = item.get("parents")
    categories.append(name)

#merge list of lists
categories = list(itertools.chain(*categories))

#remove duplicate parent category items
def remove_duplicates(original_list):
    unique_list = []
    [unique_list.append(obj) for obj in original_list if obj not in unique_list]
    unique_list.sort()
    print unique_list

remove_duplicates(categories)



