#!/usr/bin/python3

import os
from os import listdir
import argparse as ap

parser=ap.ArgumentParser()
parser.add_argument("-i", "--input", help="Input directory of genomes", type=str)
args=parser.parse_args()

input_dir=args.i

dirs = listdir(input_dir)

for i in range(len(dirs)):
	if os.path.isdir(f"{input_dir}{dirs[i]}"):
		with open("files.txt", "a+") as f:
			f.write(f"{input_dir}{dirs[i]}\n")
	else:
		continue

os.system(f"fastani --ql files.txt --rl files.txt -o output.out")