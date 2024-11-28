#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('playground').makeChange

print(makeChange([1, 2, 25], 0))

print(makeChange([1256, 54, 48, 16, 102], 1453))

print(makeChange([4, 5], 7))

print(makeChange([9, 6, 1], 11))