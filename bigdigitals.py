#!/usr/bin/env python3
# by Pavel Pavlov (c) 2016
# My second  program on Python 3

import sys


Zero = ["  ***  ",
        " *   * ",
        "*     *",
        "*     *",
        "*     *",
        " *   * ",
        "  ***  "]
One =  ["    *  ",
        "   **  ",
        "  * *  ",
        "    *  ",
        "    *  ",
        "    *  ",
        "   *** "]
Two =  ["  ***  ",
        " *   * ",
        " *   * ",
        "    *  ",
        "   *   ",
        "  *    ",
        " ******"]
Three = ["  ***  ",
         " *   * ",
         "     * ",
         "   **  ",
         "     * ",
         " *   * ",
         "  ***  "]
Four = ["     * ",
        "   * * ",
        "  *  * ",
        " *   * ",
        " ******",
        "     * ",
        "     * "]
Five = [" ***** ",
        " *     ",
        " *     ",
        "  ***  ",
        "     * ",
        " *   * ",
        "  ***  "]
Six =  ["  ***  ",
        " *     ",
        " *     ",
        "  ***  ",
        " *   * ",
        " *   * ",
        "  ***  "]
Seven = [" ***** ",
         "     * ",
         "    *  ",
         "   *   ",
         "   *   ",
         "   *   ",
         "   *   "]
Eight = ["  ***  ",
         " *   * ",
         " *   * ",
         "  ***  ",
         " *   * ",
         " *   * ",
         "  ***  "]
Nine = ["  ***  ",
        " *   * ",
        " *   * ",
        "  ***  ",
        "     * ",
        "     * ",
        "  ***  "]

Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

try:
    digits = sys.argv[1]
    row = 0
    while row < 7:
        line = ""
        column = 0
        while column < len(digits):
            number = int(digits[column])
            digit = Digits[number]
            line += digit[row] + " "
            column += 1
        print(line)
        row += 1
except IndexError:
    print("usage: bigdigits.py <number>")
except ValueError as err:
    print(err, "in", digits)
