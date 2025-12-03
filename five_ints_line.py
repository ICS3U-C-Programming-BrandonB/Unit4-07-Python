#!/usr/bin/env python3
# Created By: Brandon
# Date: 12/01/2025
# Program to show all valid color combos


def main():
    # for loop to move through years 1000 to 2000
    for year in range(1000, 2001, 1):
        if year % 5 == 0 and year != 1000:
            # print a newline before the year if it's divisible by 5
            print("\n", year, end=" ")
        else:
            print(year, end=" ")


if __name__ == "__main__":
    main()
