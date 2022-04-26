#!/usr/bin/env python3

# Author:  Kenji Nishiura
# Description:  identifies E. Coli MLST profile, and then infers approximately-maximum-likelihood phylogenetic tree using GTR substitution model
#
# anaconda package names of dependencies:
# fastmlst
# mafft
# trimal
# FastTree
# pandas
# dataframe_image

import argparse
import os
import pandas as pd
import dataframe_image as dfi

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--cpus", help="number of threads", type=int, default=4)
parser.add_argument(
    "-f",
    "--input_fasta",
    metavar="<fasta input>",
    help="Path to genome assembly fasta files (ex:  contigs/*.fa)",
    required=True,
)
parser.add_argument(
    "-o",
    "--output_fasta",
    metavar="<fasta output>",
    help="Filename for concatenated gene fasta output",
    required=True,
)
parser.add_argument(
    "-t",
    "--output_tab",
    metavar="<tabular output>",
    help="Filename for tabular output",
    required=True,
)
parser.add_argument(
    "-z",
    "--output_tree",
    metavar="<tree output>",
    help="Filename for tree output",
    required=True,
)
args = parser.parse_args()

# update  MLST database
updateDB = f"fastmlst --update-mlst"
os.system(updateDB)

# run fastmlst
mlst = f"fastmlst -t {args.cpus} -v 2 -sch ecoli#1 -fo {args.output_fasta} -to {args.output_tab} -n novel.fasta {args.files}"
os.system(mlst)

# load fastmlst tabular output, store in dataframe, save as image
df=pd.read_csv(f"{args.output_tab}",header=0,index_col=0)
dfi.export(df,f"{args.output_tab}.png",table_conversion = 'matplotlib')

# align concatenated gene fasta file
align = f"mafft --auto --thread {args.cpus} {args.output_fasta} > tmp.aln"
os.system(align)

# trim alignment
trim = f"trimal -in tmp.aln -out tmp_trimmed.aln -automated1"
os.system(trim)

# build tree
tree = f"FastTree -nt -gtr < tmp_trimmed.aln > {args.output_tree}"
os.system(tree)
