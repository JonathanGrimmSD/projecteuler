#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division

__author__ = "Jonathan Grimm"
__date__ = "07.02.18"
import math


# 041: Pandigital prime
def primes2(n):
    #credit to 'Robert William Hanks' https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    n, correction = n - n % 6 + 6, 2 - (n % 6 > 1)
    sieve = [True] * (n // 3)
    for i in xrange(1, int(n ** 0.5) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[k * k // 3::2 * k] = [False] * ((n // 6 - k * k // 6 - 1) // k + 1)
            sieve[k * (k - 2 * (i & 1) + 4) // 3::2 * k] = [False] * (
            (n // 6 - k * (k - 2 * (i & 1) + 4) // 6 - 1) // k + 1)
    return [2, 3] + [3 * i + 1 | 1 for i in xrange(1, n // 3 - correction) if sieve[i]]


def project041():
    primes=primes2(40)
    return primes

project041()
# 042: Coded triangle numbers
def triangleNumber(x):
    erg1=-1/2+math.sqrt(1/4+2*x)
    erg2=-1/2-math.sqrt(1/4+2*x)
    if erg1>0:
        return erg1 == int(erg1)
    elif erg2>0:
        return erg2 == int(erg2)


def project042():
    f = open("project042.txt", 'r')
    nbr=0
    names = f.readline().replace('"', '').split(',')
    for name in names:
        value=0
        for char in name:
            value+=ord(char)-64
        if triangleNumber(value):
            nbr+=1
    return nbr


# 47: Distinct primes factors
def project047():
    pass

# 048: Self powers
def project048(prec=10):
    selfpower=0
    for x in xrange(1,1001):
        nsp=1
        for n in xrange(x):
            nsp *= x
            if len(str(nsp))>prec:
                nsp=int(str(nsp)[-prec:])
        selfpower+=nsp

    selfpower=str(selfpower)
    if len(selfpower)>prec:
        selfpower=selfpower[-prec:]
    while len(selfpower)<prec:
        selfpower="0"+selfpower
    return selfpower


import time
t=time.time()
print project041()
#print project042()
# print project048()
print time.time()-t

t=time.time()
print project041b()
print time.time()-t

