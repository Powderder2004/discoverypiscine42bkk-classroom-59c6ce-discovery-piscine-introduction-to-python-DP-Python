import sys

def main():
    if len(sys.argv) <= 1:
        print("none")
    else:
        print(sys.argv[1])

if __name__ == "__main__":
    main()