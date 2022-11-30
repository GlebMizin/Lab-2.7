#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":

    punc_marks = set(".?,!:;`'  ")

    # Input
    s_1 = set(input("Enter the first string: "))
    s_2 = set(input("Enter the second string: "))

    # Finding intersection between s_1 and s_2
    inter = s_1.intersection(s_2)

    # Remove all punctuation marks
    clear_set = inter.difference(punc_marks)

    # Output of intersection
    print(f"Same string characters: {clear_set}")
