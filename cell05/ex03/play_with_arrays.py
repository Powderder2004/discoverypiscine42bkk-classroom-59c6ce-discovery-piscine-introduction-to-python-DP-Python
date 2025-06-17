def main():
    original = [2, 8, 9, 48, 8, 22, -12, 2]
    new_set = {x + 2 for x in original if x >= 8}

    print(original)
    print(new_set)

if __name__ == "__main__":
    main()