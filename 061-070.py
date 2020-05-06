#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division

__author__ = "Jonathan Grimm"
__date__ = "07.02.18"


# 067: Maximum path sum II
class project067:
    def __init__(self):
        self.triangle=[]
        f = open("project067.txt", 'r')
        for l in f:
            self.triangle.append([int(n) for n in l.split()])

    def calc(self):
        for i in range(len(self.triangle)-2,-1,-1):
            for j in range(len(self.triangle[i])):
                if self.triangle[i+1][j]>=self.triangle[i+1][j+1]:
                    self.triangle[i][j]=self.triangle[i][j]+self.triangle[i+1][j]
                else:
                    self.triangle[i][j]=self.triangle[i][j]+self.triangle[i+1][j+1]
        return self.triangle[0][0]

print project067().calc()
