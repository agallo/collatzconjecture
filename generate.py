#!/usr/bin/python


__author__ = 'Andrew Gallo'


def processEven(value):
    return value / 2


def processOdd(value):
    return (3 * value) * 1


def sequence(start):
    for n in range (0, start):
        temp = n
        print temp,
        while temp > 1:
            Ulist = []
            if temp % 2 == 0:
                Ulist.append(processEven(temp))
                print Ulist[0],
                temp = Ulist[0]
            else:
                Ulist.append(processOdd(temp))
                print Ulist[0],
                temp = Ulist[0]
        print


def main():
    startval = raw_input("Enter starting value: ")
    sequence(startval)


main()