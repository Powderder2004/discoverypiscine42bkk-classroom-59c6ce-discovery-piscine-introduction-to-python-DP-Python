import sys

def main():
    args = sys.argv[1:]  # ตัดชื่อไฟล์ออก (index 0 คือชื่อไฟล์)
    print(f"Number of parameters: {len(args)}.")

if __name__ == "__main__":
    main()