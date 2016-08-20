#!/usr/bin/python


__author__ = 'Andrew Gallo'

# FTO stands for four-two-one (always the end of the collatz conjecture)

import networkx as nx
import pygraphviz as pgv
from argparse import ArgumentParser


parser = ArgumentParser(description="calculate and graph numbers in the Collatz Conjecture")

parser.add_argument('start', help="starting number", type=int)

parser.add_argument('-g', '--graph', dest='gtype', type=str,
                    help='graph type neato, dot[DEFAULT], twopi, circo, fdp, nop', default='dot')

args = parser.parse_args()

startnum = args.start
gtype = args.gtype

# list of all layout (progs) in case someone uses the hidden type all
layouts = ['neato', 'dot', 'twopi', 'circo', 'fdp', 'nop']

CC = nx.DiGraph()


def sequence(start, layout):
    for n in range(5, start):
        temp = n
        Ulist = [temp]
        while temp > 1:
            if temp % 2 == 0:
                Ulist.append(temp/2)
                temp = Ulist[-1]
            else:
                Ulist.append((3 * temp) + 1)
                temp = Ulist[-1]
        Ulist = Ulist[0:-3]
        Ulist.append('FTO')
#        print Ulist
        CC.add_path(Ulist)
    A = nx.to_agraph(CC)
    if layout != 'all':
        filename = './graphs/cc' + str(start) + '-' + layout + '.png'
        A.draw(filename, prog=layout)
    else:
        for layout in layouts:
            filename = './graphs/cc' + str(start) + '-' + layout + '.png'
            A.draw(filename, prog=layout)



def main():
    sequence(startnum, gtype)


main()
