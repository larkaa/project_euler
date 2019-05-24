setwd("/home/larkaa/python_learning")

#1 Find the sum of all the multiples of 3 or 5 below 1000.

#3*(1+2+3...)
#5*(1+2+3...)
# 1+2+3+4+... = n(n+1)/2
# note sum BELOW 1000
s = 1000-1
a = floor(s/3)
b = floor(s/5)
c = floor(s/15)
(3*a*(a+1) + 5*b*(b+1) - 15*c*(c+1))/2
# 233168, s = 1000
# 23, s = 10
# 
# First of all, stop thinking on the number 1000 and turn your
# attention to the number 990 instead. If you solve the problem
# for 990 you just have to add 993, 995, 996 & 999 to it for
# the final answer. This sum is (a)=3983
# 
# Count all the #s divisible by 3: From 3... to 990 there are
# 330 terms. The sum is 330(990+3)/2    (b)=163845 
# Count all the #s divisible by 5: From 5... to 990 there are
# 198 terms. The sum is 198(990+5)/2    (c)=98505
# 
# Now, the GCD (greatest common divisor) of 3 & 5 is 1 so the
# LCM (least common multiple) should be 3x5 15.
# This means every number that divides by 15 was counted twice
# and it should be done only once. Because of this, you have an
# extra set of numbers started with 15 all the way to 990 that
# has to be removed from (b)&(c).
# Then, from 15... to 990 there are 66 terms and the sum is
# 66(990+15)/2    (d)=33165
# 
# The answer for the problem is: (a)+(b)+(c)-(d) = 233168


##2 By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
# 0,1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
# every 3rd number is even!

2 = F(3*1)
2^3 = F(3*2) = F(3)^3
2^5+2 = F(3*3)

len=1000000
f = numeric(len)
f[1]=1
f[2]=1

for (i in 3:len) { 
  f[i] <- f[i-1]+f[i-2]
  if(f[i]>4000000){break}
} 
#f[33]<4 million
sum(f[seq(3, 33, 3)])

# alternative: golden ratio, golden ratio^3

#3. What is the largest prime factor of the number 600851475143 ?What is the largest prime factor of the number 600851475143 ?
num = 600851475143
#num=100
#num = 13195

largest_prime = function(n){
  i=2
  while (i*i<n){
    if (n%%i != 0)
      i = i+1
    else n=n/i
  }
  return(n)
}
largest_prime(num)


## question 4: Find the largest palindrome made from the product of two 3-digit numbers
#python

# question 5: smallest number evenly divisible by 1 to 20
2^4*3^2*5*7*11*13*17*19 


### question 8
# largest 13-series with highest product

str = "73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450"

str = gsub("[\r\n]", "", str)

num = 1
for (i in 1:(nchar(str)-14)){
  temp = substr(str,i,12+i)
  newnum = prod(as.numeric(unlist(strsplit(temp,split=""))))
  #print(newnum)
  if (newnum >= num){
    num=newnum
  }
}
num 
# 23514624000




## quesiton 9
# pythagorean triplet where a+b+c=1000? find a*b*c
# list of squares <1000, 
squares = seq(1,1000)*seq(1,1000)
simple = seq(1,1000)


for (i in 1:1000){
  for (j in i:1000){
    temp = squares[i]+squares[j]
    if (temp %in% squares){ ## first check
      temp2 = sqrt(squares[i]+squares[j])
      if (i+j+temp2==1000){ ## second check
        print(cbind(i,j,temp2,i*j*temp2))
        i=999999
      }
    }
  }
}

# answer
# i   j temp2         
# [1,] 200 375   425 31875000

# alternate is algebraic



