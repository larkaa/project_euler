#!/usr/bin/env python3

#question 22 name score

# p022_names.txt import
# sort names
# calculate the name number abc = 1+2+3 = 6
# multiply by it's row in the file to find the name score


# What is the total of all the name scores in the file?

import string
values = dict()
for index, letter in enumerate(string.ascii_uppercase):
  values[letter] = index+1
#print(values['A'])
#print( sum([(values[x]) for x in 'AARON']))

filename = 'p022_names.txt'
rawnames = open(filename).read()
rawnames = rawnames.strip('"')
names = rawnames.split('","')
# there is still a name "MARY
#import csv
#with open(filename, 'rb') as rawnames:
#  spamreader = csv.reader(filename, delimiter=',', quotechar='"')
#  for row in spamreader:
    

#print(names[0])

#print(type(names))

names.sort()
#print(names[-1],names[0])

name_length = len(names)
name_scores = [0]*name_length
for i in range(name_length):
  temp = names[i]
  #print(i,names[i])
  name_scores[i] = sum([(values[x]) for x in temp]) * (i+1)

#print(len(names),names[0],name_scores[0],names[-1],name_scores[-1])
#print(name_scores[10])
print(sum(name_scores))
# 871198282 YAY


#temp = all_factors(284)
#print(temp,sum(temp),sum(all_factors(220)))


