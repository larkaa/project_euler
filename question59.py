#!/usr/bin/env python3

# XOR decryption
#Problem 59
#Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

#A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

#For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.

#Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

#Your task has been made easy, as the encryption key consists of three lower case characters. Using cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.

import time
import csv
start_time = time.time()

filename = 'p059_cipher.txt'
f=open(filename)
for row in csv.reader(f):
    rawfile = row


#print(rawfile)
#rawfile= open(filename).read()
#rawfile = rawfile.strip("'")
data = [int(x) for x in rawfile]
#rawfile.split('","')

#a = data
from itertools import groupby

y = [len(list(group)) for key, group in groupby(data)]


def cipher(word,key):
  res = 0
  for i in range(len(word)):
    temp = int(word[i])^ord(key[i%len(key)])
    print(chr(temp), end=' ')
    res += temp
  return res


def freq(word):
  i=0
  res = []
  while i+4<len(word):
    res.append(word[i:i+3])
    i+=3
  
  return sorted(res)


#t1 = 0^ord('a') #int(data[0])^int(data[3])
#t2 = 7^ord('n') #int(data[1])^int(data[4])
#t3 = 16^ord('d') #int(data[2])^int(data[5])


#print(freq(data))
final = cipher(data,'god')
print(final)
#print(chr(t1),chr(t2),chr(t3))  

print('xxxxx',int(data[1])^ord('T'))
print ('  %s seconds ---' % (time.time()-start_time))

#2, 7, 1: 103, 98, 100: g b d


# 107359 YAY


