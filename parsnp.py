#!/usr/bin/env python3

#Python Script Example: ./parsnp.py -c /home/aharris334/Parsnp-Linux64-v1.2/parsnp -r /home/groupb/analysis/Team2-ComparativeGenomics/GCF_003697165.2.fa  -d /home/aharris334/genomes -o /home/aharris334/parSNP_out -p 6

#Commands in the shell:./parsnp.py -c /opt/anaconda3/bin -r /Users/adrianharris/Desktop/AE005174/AE005174.fna -d /Users/adrianharris/Desktop/genomes -o /Users/adrianharris/Desktop/parSNP_filter_50isolates -p 6 -x

import argparse as ap
import subprocess as sp
import time
import os

parser = ap.ArgumentParser()
parser.add_argument("-c", "--parsnp", help="path to ParSNP command", required=True)
parser.add_argument("-r", "--ref", help="path to the reference genome", required=True)
parser.add_argument("-d", "--genomes", help="path to directory of genomes", required=True)
parser.add_argument("-o", "--output", help="output directory", required=True)
parser.add_argument("-p", "--threads", help="number of threads", default=1)
parser.add_argument("-f", "--filter", help="filtering regions of high recombination using PhiPack", action='store_true')
args = parser.parse_args()

start_time = time.time()

if args.filter:
	parsnp_run = sp.call([args.parsnp, "-r", args.ref, "-d", args.genomes, "-o", args.output, 
	"-p", args.threads, "-x"])
else:
	parsnp_run = sp.call([args.parsnp, "-r", args.ref, "-d", args.genomes, "-o", args.output, 
	"-p", args.threads])


print("Runtime:", time.time() - start_time)