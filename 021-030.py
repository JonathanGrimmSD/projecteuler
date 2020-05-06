#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division

__author__ = "Jonathan Grimm"
__date__ = "05.02.18"

from itertools import permutations
import decimal
import math


# 021: Amicable numbers
def d(n):
    div = 0
    for i in range(1, n):
        if n % i == 0:
            div += i
            # print i
    return div


def project021():
    sum = 0
    for a in xrange(10000):
        b = d(a)
        if d(b) == a and b != a:
            sum += a
    return sum


# 022: Name scores
def project022():
    f = open("project022.txt", 'r')
    names = f.readline().replace('"', '').split(',')
    names.sort()
    namescore = 0
    for i, n in enumerate(names):
        namevalue = 0
        for c in n:
            namevalue += ord(c) - 64
        namescore += (i + 1) * namevalue
    return namescore


# 023: Non-abundant sums
class project023:
    def __init__(self):
        self.abundant_list = {i for i in range(28124) if self.check_if_abundant(i)}

    def check_if_abundant(self, n):
        if n == 0:
            return 0
        sum1 = 1  # sum of factors of n
        for i in range(2, int(n ** 0.5) + 1):
            if (n % i) == 0:
                sum1 += i
                if n / i != i:
                    sum1 += n / i
        return sum1 > n

    def check_nonabundant_sum(self, x):
        for i in self.abundant_list:
            if x <= i:
                return True
            elif x - i in self.abundant_list:
                return False
        return True

    def calc(self):
        summe = 0
        for i in range(28124):
            if self.check_nonabundant_sum(i):
                summe += i
        return summe


# 024: Lexicographic permutations
def project024():
    lst = range(10)
    m = list(permutations(lst))
    return str(m[999999]).replace(", ", "").replace("(", "").replace(")", "")


# 025: 1000-digit Fibonacci number
def project025():
    n = 3
    f2 = 1
    f1 = 1
    while True:
        fn = f1 + f2
        if len(str(fn)) >= 1000:
            break
        f2 = f1
        f1 = fn
        n += 1
    return n


# 026: Reciprocal cycles
def getdigit(x, n0):
    return str(x)[n0]

def longdivision(zaehler, nenner, precision=1000):
    n = 0
    div = 0
    erg = ""
    dotset=False
    reste=[]
    ilen=0

    while True:
        div *= 10
        if n==len(str(zaehler)):
            zaehler*=10
            if not dotset:
                erg+="."
                dotset=True
        digit = getdigit(zaehler, n)
        if digit == ".":
            erg += "."
            dotset=True
        else:
            div += int(getdigit(zaehler, n))
            if div in reste:
                i=reste.index(div)
                ilen=len(erg)-(i+1)
                erg=erg[:i+1]+"("+erg[i+1:]+")"
                break
            reste.append(div)
            erg += str(div // nenner)
            div = div % nenner
            if div==0:
                break
            n += 1
            #print erg

        if "." in erg:
            if precision<len(erg[erg.index("."):]):
                break
    if len(erg)>1 and erg[0]=="0" and erg[1]!=".":
        erg=erg[1:]
    return erg,ilen #reste,"\n",
#longdivision(1,31)


def project026():
    imax=0
    ilen=0
    for i in xrange(1,1001):
        x=longdivision(1,i)
        if x[1]>ilen:
            imax=i
            ilen=x[1]
    return imax


# 027: Quadratic primes
def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    sqr = int(math.sqrt(n)) + 1
    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True


def project027():
    ab = [0, 0, 0]
    for a in range(-999, 1000, ):
        for b in range(-1000, 1001):
            n = 0
            while True:
                c = n ** 2 + a * n + b
                if is_prime(c):
                    n += 1
                    if n > ab[-1]:
                        ab = [a, b, n]
                else:
                    break
    return ab[0] * ab[1]


# 028: Number spiral diagonals:
def project028():
    width = 1001
    res = [1]
    for i in xrange(1, int(((width - 1) / 2) + 1)):
        for n in xrange(4):
            res.append(res[-1] + 2 * i)
    return sum(res)


# 029: Distinct powers
def project029():
    seq = []
    for a in xrange(2, 101):
        for b in xrange(2, 101):
            if a ** b not in seq:
                seq.append(a ** b)
    return len(seq)


# 030: Digit fifth powers
def check030(x, power):
    checksum = 0
    for i in range(len(str(x))):
        checksum += int(str(x)[i]) ** power
    return checksum == x


def project030():
    power = 6
    n = 1
    while n * 9 ** power > 10 ** n:
        n += 1
    erg = 0

    for i in range(10, 10 ** n):
        if check030(i, power):
            erg += i
    return erg

# print project021()
# print project022()
# print project023().calc()
# print project024()
# print project025()
print project026()
# print project027()
# print project029()
# print project028()
# print project030()
