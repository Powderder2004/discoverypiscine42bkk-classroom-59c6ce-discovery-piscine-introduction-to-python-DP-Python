#!/usr/bin/env python3

def add_one(x):
    x += 1

if __name__ == "__main__":
    num = 5
    print(num)      # Display before calling add_one
    add_one(num)    # Call add_one, trying to increment num
    print(num)      # Display after calling add_one
