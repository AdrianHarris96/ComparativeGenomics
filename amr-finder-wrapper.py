#!/usr/bin/env python3

import argparse
import os
# uncomment this block if tabular output as image is desired
# import dataframe_image as dfi
# import pandas as pd
# import matplotlib

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input_dir', metavar = '<directory>', 
    help = "Path to directory containing contigs",required=True)
parser.add_argument('-o', '--organism', metavar = '<AMRFinder Organism ID>', default = 'Escherichia',
    help = "Organism identifier to be used in AMRFinder: Default = Escherichia")
args = parser.parse_args()

# download database from NCBI
create_amr_db= f'amrfinder --force_update'
os.system(create_amr_db)

# Loops through each file in input directory, runs AMRFinder on each 
# Output goes in current directory, name is the same as input filename with .out suffix
run_amr_finder=f'for assembly in {args.input_dir}/*; do amrfinder -n "$assembly" --organism {args.organism} --output "$(basename $assembly)".out; done'
os.system(run_amr_finder)

# uncomment this block if tabular output as image is desired
# # load output tsv, store in dataframe, save as image
# df=pd.read_csv("sample", sep="\t",header=0,index_col=0)
# dfi.export(df,"amr_finder_out.png",table_conversion = 'matplotlib')