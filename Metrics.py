import sys
from sklearn import metrics

def get_metrics(approx_logline_mapping, approx_partition_mapping, true_logline_mapping, true_partition_mapping):
    approx_labels = []
    true_labels = []

    loglines = [x for x in approx_logline_mapping.keys()]
    loglines.sort()
    for logline in loglines:
        approx_labels.append(approx_logline_mapping[logline])
        true_labels.append(true_logline_mapping[logline])

    print("Rand score: " + str(metrics.rand_score(approx_labels, true_labels)))
    print("Adjusted rand score: " + str(metrics.adjusted_rand_score(approx_labels, true_labels)))
    print("Adjusted mutual information score: " + str(metrics.adjusted_mutual_info_score(approx_labels, true_labels)))
    print("Fowlkes Mallows score: " + str(metrics.fowlkes_mallows_score(true_labels, approx_labels)))
    
if __name__ == "__main__":
    if (len(sys.argv) != 3):
        exit()
    approx_filename = sys.argv[1]
    true_filename = sys.argv[2]

    # Load approximated partitioning
    approx_logline_mapping = {}
    approx_partition_mapping = {}
    with open(approx_filename, "r") as f:
        for line in f:
            logline, partition = line.split(",")
            logline = int(logline)
            partition = int(partition.strip())

            approx_logline_mapping[logline] = partition
            if (partition in approx_partition_mapping.keys()):
                approx_partition_mapping[partition].append(logline)
            else:
                approx_partition_mapping[partition] = [logline]

    # Load true partitioning
    true_logline_mapping = {}
    true_partition_mapping = {}
    with open(true_filename, "r") as f:
        for line in f:
            logline, partition = line.split(",")
            logline = int(logline)
            partition = int(partition.strip())

            true_logline_mapping[logline] = partition
            if (partition in true_partition_mapping.keys()):
                true_partition_mapping[partition].append(logline)
            else:
                true_partition_mapping[partition] = [logline]

    # Get metrics
    get_metrics(approx_logline_mapping, approx_partition_mapping, true_logline_mapping, true_partition_mapping)