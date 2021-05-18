import sys
import random

if __name__ == "__main__":
    num_templates = int(sys.argv[2])
    outfile = sys.argv[1]
    mapping = {}
    for i in range(0, num_templates):
        filename = "results/drain/template" + str(i+1) + ".txt"
        lines = []
        with open(filename, "r") as f:
            lines = f.readlines()
        
        for j in range(0, len(lines)):
            line_num = int(lines[j].strip())
            mapping[line_num + 1] = i

    with open(outfile, "w") as f:
        for i in range(1, 101):
            f.write(str(i) + "," + str(mapping[i]) + "\n")