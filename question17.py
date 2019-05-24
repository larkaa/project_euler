#!/usr/bin/env python3

#question 17
# count the number of letters in the numbers 1 to 1000
# format
# one hundred and thirty one

digits_str = ['','one','two','three','four','five','six','seven','eight','nine']
teens_str = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
tens_str = ['','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety']

 
digits = [len(x) for x in digits_str]
teens = [len(x) for x in teens_str]
tens =  [len(x) for x in tens_str]
hundred = 7
hundred_and = 10
# X hundred *(1+(3+ninty nine others))
one_thou = len('onethousand')

total_sum = 0

# digits and teens
total_sum+= sum(digits) + sum(teens)

# tens are in the form twenty, thrity, then 
#  twenty twenty-one two...nine, thirty-one two... nine,
# = twenty appears 10 times more
# but the number one appears 8 times more for each twenty, 
# so 8*9

#total_sum += sum(tens) + 9*(sum(tens) + 8*sum(digits))
#sumto99 = total_sum
#print(sumto99)
#3168
total_sum = 864
sumto99 = 864

# hundreds are of the form 
# one hundred, two, three... nine 
# one hundred AND one... ninety nine... nine hundred AND one... ninety nine
# -> hundred appears nine times more digits one time
# -> sumto99 appears 9 times more + hundred_and *90 (less 9 bc not including 100,200,300)
#total_sum += 9*(hundred + sum(digits)) #hundreds without and
#total_sum += 9*sumto99 + 90*hundred_and # hundreds with and

# otherwise, one hundred 99 times, , with 'and' 9 times
total_sum += 99*(sum(digits)+hundred) + 9*hundred_and + 9*sumto99

# one thousand once
total_sum += one_thou

print(total_sum)



#brute force backwards
total2 = one_thou




 
def to99(num):
  #print(num)
  temp = 0
  for i in range(1,100):
    if i<10:
      temp+= (digits[i])
      #print(digits_str[i])
    elif i<20 and i>=10:
      temp+= (teens[i%10])
      #print(teens_str[i%10])
    else:
      #print(i,i//10,i%10)
      temp+= (tens[i//10-1]) + (digits[i%10])
      #print(tens_str[i//10-1],digits_str[i%10])
  return(temp)

temp = 0
for hund in digits_str:
  sumto99 = to99(10)
  if len(hund)==0:
    temp+= sumto99
  elif len(hund)>0: 
    temp += len(hund)
    temp += len('hundred') # case of 1 hundred, 2 hundred...
    temp += 99*(len('and') + len(hund)) 
    temp += sumto99

print(temp)



#864

to99(10)
 
