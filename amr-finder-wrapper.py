#!/usr/bin/env python3

import argparse
import os
# uncomment this block if tabular output as image is desired
# import dataframe_image as dfi
# import pandas as pd
# import matplotlib

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input_dir', metavar = '<directory>', 
    help = "Path to directory contianing contigs")
parser.add_argument('-o', '--organism', metavar = '<AMRFinder Organism ID>', default = 'Escherichia',
    help = "Organism identifier to be used in AMRFinder: Default = Escherichia")
args = parser.parse_args()

run_amr_finder = f'ls {args.input} | xargs -I sample amrfinder -n {args.input}/contigs.fa --organism {args.organism} --output sample'
os.system(run_amr_finder)

# uncomment this block if tabular output as image is desired
# # load output tsv, store in dataframe, save as image
# df=pd.read_csv("sample", sep="\t",header=0,index_col=0)
# dfi.export(df,"amr_finder_out.png",table_conversion = 'matplotlib')