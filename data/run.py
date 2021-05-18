import sys
import random

if __name__ == "__main__":
    filename = sys.argv[1]

    lines = []
    with open(filename, "r") as f:
        lines = f.readlines()
    
    for i in range(0, len(lines)):
        lines[i] = str(i+1) + " " + " ".join(lines[i].strip().split()[1:]) + "\n"

    with open(filename, "w") as f:
        f.writelines(lines)