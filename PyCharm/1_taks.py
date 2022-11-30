#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":

    # All vowels letters
    vowels = set("aeiouyYUOIEA")

    # Input
    s = input("Enter the string: ")

    # Finding amount of vowels
    kol_vo = 0
    for i in s:
        if i in vowels:
            kol_vo += 1

    # Output
    print(f"Number of vowels: {kol_vo}")
