#!/usr/bin/env python3

# Almost equilateral triangles
#Problem 94
#It is easily proved that no equilateral triangle exists with integral length sides and integral area. However, the almost equilateral triangle 5-5-6 has an area of 12 square units.

#We shall define an almost equilateral triangle to be a triangle for which two sides are equal and the third differs by no more than one unit.

#Find the sum of the perimeters of all almost equilateral triangles with integral side lengths and area and whose perimeters do not exceed one billion (1,000,000,000).


squares=[ i*i for i in range(int(1000000000**.5)) ]

import math
import time
start_time = time.time()

count=0

for side in range(3, 1000000000//3): #1000000000):
  p1 = (3*side+1)/2
  p2 = (3*side-1)/2
  a1 = p1*(p1-side)**2*(p1-(side+1))
  a2 = p2*(p2-side)**2*(p2-(side-1))

  #if math.sqrt(a1)==int(math.sqrt(a1)): count+=p1*2; #print(side,side,side+1)
  #if math.sqrt(a2)==int(math.sqrt(a2)): count+=p2*2; #print(side,side,side-1)
  if a1 in squares: count+=p1*2; #print(side,side,side+1)
  if a2 in squares: count+=p2*2; #print(side,side,side-1)
  
print(count)



def pytrip(trip=(3,4,5),perim=100, prim=1):
    a0, b0, c0 = a, b, c = sorted(trip)
    t, firstprim = set(), prim>0
    while a + b + c <= perim:
        t.add((a, b, c, firstprim>0))
        a, b, c, firstprim = a+a0, b+b0, c+c0, False
    #
    t2 = set()
    for a, b, c, firstprim in t:
        a2, a5, b2, b5, c2, c3, c7 = a*2, a*5, b*2, b*5, c*2, c*3, c*7
        if  a5 - b5 + c7 <= perim:
            t2 |= pytrip(( a - b2 + c2,  a2 - b + c2,  a2 - b2 + c3), perim, firstprim)
        if  a5 + b5 + c7 <= perim:
            t2 |= pytrip(( a + b2 + c2,  a2 + b + c2,  a2 + b2 + c3), perim, firstprim)
        if -a5 + b5 + c7 <= perim:
            t2 |= pytrip((-a + b2 + c2, -a2 + b + c2, -a2 + b2 + c3), perim, firstprim)
    return t | t2
 
def pt2(maxperimeter=100):
    '''
# Parent/child relationship method:
# http://en.wikipedia.org/wiki/Formulas_for_generating_Pythagorean_triples#XI.
    '''
    trips = pytrip((3,4,5), maxperimeter, 1)
    return trips
 
def printit(maxperimeter=100, pt=pt2):
    trips = pt(maxperimeter)
    print("  Up to a perimeter of %i there are %i triples, of which %i are primitive"
          % (maxperimeter,
             len(trips),
             len([prim for a,b,c,prim in trips if prim])))
 


#print(pt2.__doc__)
#printit(1000000000,pt2)



print ('--- %s seconds ---' % (time.time()-start_time))
