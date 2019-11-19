#!/bin/python

#Emily Wambach 
#Lab6A 
#Listing Pythagorean triple containing positive integers under 20

#declare varaibles side a, b, and c
a=0
b=0
c=0
triples=[]

for a in range (1,21): #loop for a range 
    for b in range (a,21): #loop for b range
        for c in range (b,21): #loop for c range
            if a*a+b*b==c*c: #if a^2 + b^2 =  c^2
                print triples.append([a,b,c]) #print
