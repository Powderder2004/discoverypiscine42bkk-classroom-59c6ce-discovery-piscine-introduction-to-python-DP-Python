def main():
    original = [2, 8, 9, 48, 8, 22, -12, 2]
    new_array = [x + 2 for x in original if x >= 8]

    print(original)
    print(new_array)

if __name__ == "__main__":
    main()