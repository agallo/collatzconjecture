#!/usr/bin/python


__author__ = 'Andrew Gallo'

import networkx as nx
import pygraphviz as pgv


CC = nx.DiGraph()


def processEven(value):
    return value / 2


def processOdd(value):
    return (3 * value) + 1


def sequence(start):
    for n in range(5, start):
        temp = n
        Ulist = [temp]
        while temp > 1:
            if temp % 2 == 0:
                Ulist.append(processEven(temp))
                temp = Ulist[-1]
            else:
                Ulist.append(processOdd(temp))
                temp = Ulist[-1]
        Ulist = Ulist[0:-3]
        Ulist.append('FTO')
        print Ulist
        CC.add_path(Ulist)
    one = A.add_subgraph(firsthopASNs)
    A.draw('cc.png', prog='dot')


def main():
    startval = input("Enter starting value: ")
    sequence(startval)


main()
