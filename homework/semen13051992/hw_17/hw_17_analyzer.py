import os
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("file", help="File name")
parser.add_argument("-t", "--text", help="text for search")
args = parser.parse_args()

for file in os.listdir(args.file):
    if file.endswith('.log'):
        file_log = os.path.join(args.path, file)
        with open(file_log, 'r') as log_file:
            for line in log_file:
                line = line.strip()
                date = re.findall(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{3}', line)
                text = 'ERROR'
                if args.text in line:
                    index = line.index(args.text)
                    print(date, line[index - 5: index + len(args.text) + 5])
