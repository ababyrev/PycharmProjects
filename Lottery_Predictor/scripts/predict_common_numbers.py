# Read numbers from CSV file and format into a list of integers.
# Convert list of integers into a dictionary with integer being a Key and its frequency being the Value.
# Print results

import csv
import re
from collections import Counter

csv_file = 'C:\\Users\Alex&Nat\Downloads\Lottery_Mega_Millions_Winning_Numbers__Beginning_2002.csv'

# Parse CSV file for lottery results column and append numbers to a list
numbers = []
with open(csv_file, 'rt') as f:
    reader = csv.reader(f)
    for row in reader:
        if re.match("^[0-9 ]+$", row[1]): # Match only rows with number followed by single space i.e: 1 2 3 4 5.
            numbers.append(row[1])

mylist = ' '.join(numbers).split(' ')

mylist = [x.lstrip('0') for x in mylist] # Remove leading zeros i.e. 02 becomes 2

num_list = [int(x) for x in mylist] # convert list to integers
mydict = Counter(num_list) # Converts list into dictionary with Key being the number and frequency is the Value.
#print("Unsorted: %s" % mydict)
dict_sort_by_value = {k: v for k, v in sorted(mydict.items(), key=lambda item: item[1])}
#print("Sorted by value: %s" % dict_sort_by_value)
most_frequent_value = max(mydict.keys(), key=(lambda k: mydict[k]))
print("Most common number: %s" % most_frequent_value)
print("Occurences: %s" % mydict[most_frequent_value])

print("Top 5 most common numbers:")
print("{:>2}{:>15}".format('Number','Frequency'))
for x in list(reversed(list(dict_sort_by_value)))[0:5]:
    print("{:>2}{:>13}".format(x, mydict[x]))
