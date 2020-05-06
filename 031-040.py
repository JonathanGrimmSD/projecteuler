#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division

__author__ = "Jonathan Grimm"
__date__ = "07.02.18"
import math


# 031: Coin sums:
def count(S, m, n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if m <= 0 and n >= 1:
        return 0
    return count(S, m - 1, n) + count(S, m, n - S[m - 1])


def project031():
    d = [200, 100, 50, 20, 10, 5, 2, 1]
    m = len(d)
    return count(d, m, 200)


# 032: Pandigital products:
def project032():
    erg=[]
    for i in range(1,100):
        for j in range(100,10000):
            temp=str(i)+str(j)+str(i*j)
            if "0" not in temp:
                if len(temp)==9 and len(set(temp))==9:
                    if i*j not in erg:
                        erg.append(i*j)
    return sum(erg)


# 033: Digit cancelling fractions:
def project033():
    frac=[1,1]
    for numerator in range(10,100):
        for denominator in range(numerator+1,100):
            if numerator%10!=0 or denominator%10!=0:
                dupes=getduplicates(numerator,denominator)
                if dupes is not None:
                    num=str(numerator).replace(dupes,"")
                    den=str(denominator).replace(dupes,"")
                    if numerator/denominator==int(num)/int(den):
                        frac=[frac[0]*numerator,frac[1]*denominator]
    return frac[1]//ggt(frac[0],frac[1])


def ggt(x,y):
    if y>x:
        temp=x
        x=y
        y=temp
    while True:
        if x%y==0:
            return y
        else:
            rest=x%y
            x=y
            y=rest


def getduplicates(x,y):
    xy=str(x)+str(y)
    myset=set(xy)
    duplicates=[]
    for each in myset:
        count = xy.count(each)
        if count==2:
            duplicates.append(each)
    if len(duplicates)==1 and xy.count("0")==0 and str(x).count(duplicates[0])==1:
        return duplicates[0]
    else:
        return


# 034: Digit factorials
def nfak(n):
    fak = 1
    i = 1
    while i < n + 1:
        fak *= i
        i += 1
    return fak


def check034(x):
    res = 0
    for i in xrange(len(str(x))):
        res += nfak(int(str(x)[i]))
    return res == x


def project034():
    n = 1
    while n * nfak(9) > 10 ** n:
        n += 1
    res = 0
    for i in xrange(3, 10 ** n):
        if check034(i):
            res += i
    return res


# 035: Circular primes:
class project035:
    def __init__(self):
        self.digits = "024568"  # if one of these is last digit it cant be a prime number
        self.primes = []
        for i in xrange(1000000):
            if self.is_prime(i) and self.intersect(i):
                self.primes.append(i)

    def intersect(self, x):
        if len(str(x)) == 1:
            return True
        else:
            return not (len(set(str(x)).intersection(set(self.digits))) > 0)

    def is_prime(self, n):
        if n == 2:
            return True
        if n % 2 == 0 or n <= 1:
            return False
        sqr = int(math.sqrt(n)) + 1
        for divisor in range(3, sqr, 2):
            if n % divisor == 0:
                return False
        return True

    def rotation(self, n):
        n = str(n)
        r = [int(n)]
        for i in range(len(n) - 1):
            n = n[1:] + n[0]
            r.append(int(n))
        return list(set(r))

    def calc(self):
        res = 0
        n = 0
        while True:
            if n + 1 >= len(self.primes):
                break
            prm = self.rotation(self.primes[n])
            if set(prm).issubset(self.primes):
                res += len(prm)
                self.primes = [x for x in self.primes if x not in prm]
            else:
                n += 1
        return res


# 036: Double-base palindromes
def check_palindrome(x):
    if len(str(x)) == 1:
        return True
    for i in range(len(str(x)) / 2):
        if str(x)[i] != str(x)[-1 * (i + 1)]:
            return False
    return True


def project036():
    res = 0
    for i in range(0, 1000000):
        if check_palindrome(i):
            if check_palindrome(int("{0:b}".format(i))):
                print i, " --- ", int("{0:b}".format(i))
                res += i
    return res


# 037: Truncatable primes:
from math import sqrt;
from itertools import count, islice


def isPrime(n):
    return not (n > 1 and all(n % i for i in islice(count(2), int(sqrt(n) - 1))))


def primes2(n):
    #credit to 'Robert William Hanks' https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    n, correction = n - n % 6 + 6, 2 - (n % 6 > 1)
    sieve = [True] * (n / 3)
    for i in xrange(1, int(n ** 0.5) / 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[k * k / 3::2 * k] = [False] * ((n / 6 - k * k / 6 - 1) / k + 1)
            sieve[k * (k - 2 * (i & 1) + 4) / 3::2 * k] = [False] * (
            (n / 6 - k * (k - 2 * (i & 1) + 4) / 6 - 1) / k + 1)
    return [2, 3] + [3 * i + 1 | 1 for i in xrange(1, n / 3 - correction) if sieve[i]]


def project037(p=100):
    while True:
        primes = primes2(p)
        x = primes
        x = x[4:]

        for n in range(len(x) - 1, -1, -1):
            a = [(x[n] // (10 ** i)) % 10 for i in range(int(math.ceil(math.log(x[n], 10))) - 1, -1, -1)]
            b = set([0, 4, 6, 8])
            if len(set(a).intersection(b)) > 0:
                del x[n]
            elif a[0] == 1 or a[-1] == 1:
                del x[n]
        trunc = []
        for i in x:
            n = i
            cond = True
            for j in xrange(len(str(n)) - 1):
                if isPrime(int(str(n)[:j + 1])):
                    cond = False
                    break
                if isPrime(int(str(n)[j + 1:])):
                    cond = False
                    break
            if cond:
                trunc.append(i)
        if len(trunc) >= 11:
            break
        else:
            p *= 10
    return sum(trunc)


# 038: Pandigital multiples:
def project038():
    erg=[None,None,0]
    i=0
    cond=True
    while cond:
        i+=1
        n=1
        prod=""
        while True:
            prod+=str(i*n)
            if n==1 and len(prod)>5:
                cond=False
                break
            if prod.count("0")>0:
                break
            if len(prod)!=len(set(prod)):
                break
            if len(prod)>9:
                break
            if len(prod)==9:
                if int(prod)>int(erg[2]):
                    erg=[i,range(1,n+1),prod]
                break
                #print i,range(1,n+1),prod
            n+=1
    return erg[2]


# 039: Integer right triangles:
def project039_old():
    maxlen=[0,None]
    for p in xrange(2,1000,2):
        tris=len(getTriangles(p))
        if tris>maxlen[0]:
            maxlen=[tris,p]
    return maxlen[1]


def getTriangles(p):
    erg=[]
    for a in xrange(1,p):
        b=a
        if p<math.sqrt(a**2+b**2)+a+b:
            break
        for b in xrange(a,p):
            if p>a+b>p-(a+b):
                if p==math.sqrt(a**2+b**2)+a+b:
                    erg.append([a,b,p-(a+b)])
                if p<math.sqrt(a**2+b**2)+a+b:
                    break
    return erg


def project039():
    C={}
    for a in range(1,500):
        for b in range(a,500):
            c=int(math.sqrt(a*a+b*b))
            if a*a+b*b==c*c:
                try:
                    C[a+b+c]+=1
                except KeyError:
                    C[a+b+c]=1
    p=-1
    maxvar=-1
    for i,j in C.iteritems():
        if j>maxvar:
            p=i
            maxvar=j
    return p


# 040: Champernowne's constant
def project040():
    irr = ""
    i = 1
    while len(irr) < 1000000:
        irr += str(i)
        i += 1
    fac = 1
    for i in range(0, 7):
        fac *= int(irr[(10 ** i) - 1])
    return fac

import time
t = time.time()
# print project031()
# print project032()
# print project033()
# print project034()
# print project035().calc()
# print project036()
# print project037()
# print project038()
# print project039()
# print project040()
print time.time()-t
