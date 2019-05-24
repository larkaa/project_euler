#!/usr/bin/env python3

#question 42 coded triangle numbers
#The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

#1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

#By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

#Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?





# p042_names.txt import
# calculate names, 
# calculate triangle numbers up to that point
# count name scores in triangle numbers


import string
values = dict()
for index, letter in enumerate(string.ascii_uppercase):
  values[letter] = index+1
#print(values['A'])
#print( sum([(values[x]) for x in 'AARON']))

filename = 'p042_words.txt'
rawnames = open(filename).read()
rawnames = rawnames.strip('"')
names = rawnames.split('","')
# there is still a name "MARY
    

#print(names[0])

#print(type(names))

#names.sort()
#print(names[-1],names[0])

name_length = len(names)
name_scores = [0]*name_length
for i in range(name_length):
  temp = names[i]
  #print(i,names[i])
  name_scores[i] = sum([(values[x]) for x in temp])


limit = max(name_scores)

triangles = [1]
n=1
while n<limit:
  n+=1
  triangles.append(0.5*n*(n+1))

res_sum=0

for name in name_scores:
  if name in triangles:
    res_sum+= 1

print(res_sum)
# 162







#print(len(names),names[0],name_scores[0],names[-1],name_scores[-1])
#print(name_scores[10])
#print(sum(name_scores))
# 871198282 YAY


#temp = all_factors(284)
#print(temp,sum(temp),sum(all_factors(220)))


