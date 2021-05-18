# SLCT model for log parsing

from collections import defaultdict
import os
import shutil

class SLCT:
    def __init__(self, path='./data/', support_threshold=2, logName='dummy.log', savePath='./results/slct/'):
        self.input_filename = path + logName
        self.N = support_threshold
        self.savePath = savePath


    def get_data_space(self):
        with open(self.input_filename, "r") as f:
            data_space = [line.split() for line in f.readlines()]
        n = max([len(line) for line in data_space])
        return data_space, n

    def get_dense_1_regions(self, data_space):
        word_freq = defaultdict(int)
        for i, line in enumerate(data_space):
            for j, word in enumerate(line):
                word_freq[(word, j)] += 1
        dense_1_regions = {k: v for k, v in word_freq.items() if v >= self.N}
        return dense_1_regions

    def get_clusters(self, data_space, dense_1_regions):
        # Build cluster candidates
        cluster_candidates = defaultdict(list)
        for i, line in enumerate(data_space):
            fixed_attrs = set()
            for j, word in enumerate(line):
                if (word, j) in dense_1_regions:
                    fixed_attrs.add((word, j))
            if len(fixed_attrs) >= 1:
                cluster_candidates[frozenset(fixed_attrs)].append(i)
        # Return (dense) clusters, sorted by # of fixed attributes & word position
        return sorted([(sorted(k, key=lambda x: (x[1], x)), v) for k,v in cluster_candidates.items() if len(v) >= self.N], key=lambda x: (len(x[0]),x[0]), reverse=True)

    def get_cluster_template(self, pattern, n):
        words = ["*"] * n
        for patt_idx, (string, word_idx) in enumerate(pattern):
            words[word_idx] = string
        return " ".join(words).rstrip(" *")

    def pretty_print_clusters(self, data_space, clusters, n):
        for pattern, lines in clusters:
            template = self.get_cluster_template(pattern, n)
            print(template)
            print("-"*len(template))
            for line in lines:
                pretty_line = ' '.join(data_space[line])
                print(pretty_line)
            print("="*len(pretty_line))

    def save_results(self, clusters, n):
        if os.path.exists(self.savePath):
            shutil.rmtree(self.savePath)
        os.makedirs(self.savePath)
        with open(f"{self.savePath}/logTemplates.txt", "w+") as f:
            for i, cluster in enumerate(clusters):
                pattern, lines = cluster
                template = self.get_cluster_template(pattern, n)
                f.write(template + "\n")
                with open(f"{self.savePath}/template{i+1}.txt", "w+") as g:
                    for line in lines:
                        g.write(str(line) + "\n")


    def main(self):
        data_space, n = self.get_data_space()
        dense_1_regions = self.get_dense_1_regions(data_space)
        clusters = self.get_clusters(data_space, dense_1_regions)
        # self.pretty_print_clusters(data_space, clusters, n)
        self.save_results(clusters, n)
        return 0

# # rough HDFS params
# path = './data/'
# logName = 'HDFS.log'
# savePath = './results/slct/'
# support_threshold = 10

path = './data/'
logName = 'ProcessedSampledWindowsLog.log'
savePath = './results/slct/'
support_threshold = 2

slct = SLCT(path=path, support_threshold=support_threshold, logName=logName, savePath=savePath)
slct.main()
