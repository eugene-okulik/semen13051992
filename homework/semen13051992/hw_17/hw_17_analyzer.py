import os
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("files", help="File name")
parser.add_argument("-t", "--text", help="text for search")
args = parser.parse_args()

for file in os.listdir(args.files):
    if file.endswith('.log'):
        file_log = os.path.join(args.files, file)
        with open(file_log, 'r') as log_file:
            for line in log_file:
                date = re.findall(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{3}', line)
                if args.text in line:
                    line_split = line.split()
                    index = line_split.index(args.text)
                    stat_index = index - 5
                    if stat_index < 0:
                        stat_index = 0
                    s = line_split[stat_index:index + 6]
                    print(file, str(' '.join(date)), ' '.join([str(elem) for elem in s]))
