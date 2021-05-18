import sys
import random

if __name__ == "__main__":
    filename = sys.argv[1]

    lines = []
    with open(filename, "r") as f:
        lines = f.readlines()
    
    t = 101
    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()
        if lines[i][-1] == ",":
            lines[i] = lines[i] + str(t)
            t += 1
        lines[i] = lines[i] + "\n"

    with open(filename, "w") as f:
        f.writelines(lines)