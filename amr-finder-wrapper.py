#!/usr/bin/env python3

import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input_dir', metavar = '<directory>', 
    help = "Path to directory contianing contigs")
parser.add_argument('-o', '--organism', metavar = '<AMRFinder Organism ID>', default = 'Escherichia',
    help = "Organism identifier to be used in AMRFinder: Default = Escherichia")
args = parser.parse_args()

run_amr_finder = f'ls {args.input} | xargs -I sample amrfinder -n {args.input}/contigs.fa --organism {args.organism} --output sample'
os.system(run_amr_finder)
