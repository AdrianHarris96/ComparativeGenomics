#!/usr/bin/env python3

#Python Script Example: ./ksnp.py -w /home/groupb -g genomes -k 19 -o /home/groupb/analysis/Team2-ComparativeGenomicsksnpk19_out -c 8 -n -m

#Commands in the Shell: 
#Step 1: MakeKSNP3infile <genomes_dir> in_list A
#Step 2: kSNP3 -in in_list -outdir <output_dir> -k <kmer> -CPU <num_of_cores> -NJ -ML

#NOTE: The KSNP3 directory must be in your path and activate the conda environment, ksnp!

import argparse as ap
import subprocess as sp
import time
import os

parser = ap.ArgumentParser()
parser.add_argument("-w", "--workdir", help="working directory", required=True)
parser.add_argument("-g", "--genomes", help="name of directory containing genomes", required=True) #Be sure this in in your current working directory
parser.add_argument("-k", "--kmer", help="kmer count", required=True)
parser.add_argument("-o", "--output", help="output directory", required=True)
parser.add_argument("-c", "--cpu", help="number of cpus", required=True)
parser.add_argument("-n", "--neighbor", help="optional neighbor-joining tree", action='store_true')
parser.add_argument("-m", "--max", help="optional maximum-likelihood tree", action='store_true')
args = parser.parse_args()

os.chdir(args.workdir) #Shift to working directory

makefile_run = sp.call(["MakeKSNP3infile", args.genomes, "in_list", "A"]) #Creation of a file with list of contigs and paths

#KSNP Run Below:
if args.neighbor and args.max:
	ksnp_run = sp.call(["kSNP3", "-in", "in_list", "-outdir", args.output, "-k", args.kmer, "-CPU", args.cpu, "-NJ", "-ML"])
elif args.neighbor:
	ksnp_run = sp.call(["kSNP3", "-in", "in_list", "-outdir", args.output, "-k", args.kmer, "-CPU", args.cpu, "-NJ"])
elif args.max:
	ksnp_run = sp.call(["kSNP3", "-in", "in_list", "-outdir", args.output, "-k", args.kmer, "-CPU", args.cpu, "-ML"])
else:
	ksnp_run = sp.call(["kSNP3", "-in", "in_list", "-outdir", args.output, "-k", args.kmer, "-CPU", args.cpu])





