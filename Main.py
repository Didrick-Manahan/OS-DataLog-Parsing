# Import local files
import Preprocess

# Import packages
import sys

# Primary logic function
def main(log, output_path):
    output_log = Preprocess.preprocess(log)
    with open(output_path, "w+") as f:
        f.writelines(line + "\n" for line in output_log)

# Script entry point
# Takes two arguments: The file path for the input log file, and the file name for the output log file.
if __name__ == "__main__":
    # Check number of arguments
    if len(sys.argv) != 3:
        print("Incorrect number of arguments")
        exit()
    
    # Get cmd args
    log_path = sys.argv[1]
    output_path = sys.argv[2]

    # Read log file
    log = []
    with open(log_path, "r") as f:
        for line in f:
            log.append(line.strip())

    # Main entry point
    main(log, output_path)