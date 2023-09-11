#!/usr/bin/python3

""" Script that reads stdin line by line and computes metrics """

import sys


def print_stats(dic, size):
    """ Prints information """
    print("File size: {:d}".format(size))
    for i in sorted(dic.keys()):
        if dic[i] != 0:
            print("{}: {:d}".format(i, dic[i]))


status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
                "404": 0, "405": 0, "500": 0}

count = 0
size = 0

try:
    for line in sys.stdin:
        if count != 0 and count % 10 == 0:
            print_stats(status_codes, size)

        parts = line.split()
        count += 1

        try:
            size += int(parts[-1])
        except ValueError:
            pass

        try:
            if parts[-2] in status_codes:
                status_codes[parts[-2]] += 1
        except IndexError:
            pass

    print_stats(status_codes, size)

except KeyboardInterrupt:
    print_stats(status_codes, size)
    raise
