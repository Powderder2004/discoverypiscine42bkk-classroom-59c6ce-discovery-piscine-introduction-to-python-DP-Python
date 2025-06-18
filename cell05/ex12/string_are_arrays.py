#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) != 2:
        print("none")
        return

    text = sys.argv[1]
    count_z = text.count('z')

    if count_z == 0:
        print("none")
    else:

        print('z' * count_z)
main()