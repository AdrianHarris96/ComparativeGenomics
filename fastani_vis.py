#!/usr/bin/env python3
"""
Author:  Kenji Nishiura
Generates ANI tree from fastANI output matrix.
"""

import pandas as pd
import csv
from pathlib import Path
import scipy.cluster.hierarchy as hc
from scipy.cluster.hierarchy import ClusterNode
from Bio import Phylo
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "-i",
    "--input",
    metavar="<input fastani matrix output>",
    help="provide the lower triangular matrix output from fastANI as input",
    required=True,
)
parser.add_argument(
    "-o",
    "--output",
    metavar="<output prefix>",
    help="provide the prefix for the output tree and image",
    required=True,
)
args = parser.parse_args()


def convert_scipy_to_newick(
    node=ClusterNode, parent=float, leaf=list([str]), newick=str("")
):
    if node.is_leaf():
        return f"{leaf[node.id]}:{(parent - node.dist):.2f}{newick}"
    else:
        if len(newick) > 0:
            newick = f"):{(parent - node.dist):.2f}{newick}"
        else:
            newick = ");"
        newick = convert_scipy_to_newick(node.left, node.dist, leaf, newick)
        newick = convert_scipy_to_newick(node.right, node.dist, leaf, f",{newick}")
        newick = f"({newick}"
        return newick


SampleID = []
ani_row = []
with open(f"{args.input}", "r") as f:
    reader = csv.reader(f, delimiter="\t")
    genome_num = int(next(reader)[0].rstrip("\n"))

    for row in reader:
        SampleID.append(Path(row[0]).with_suffix("").name.rstrip(".fa"))
        ani_values = list(map(lambda d: float(d), row[1:]))
        ani_values.extend([0] * (genome_num - len(ani_values)))
        ani_row.append(ani_values)

df = pd.DataFrame(data=ani_row, columns=SampleID, index=SampleID)

# fill in diagonal and mirror values across diagonal
for selfmatch in range(genome_num):
    df.iat[selfmatch, selfmatch] = 100
for i, id in enumerate(SampleID):
    for j, ani in enumerate(df[id][i:]):
        df.iat[i, i + j] = ani

# Hierarchical clustering
linkage = hc.linkage(df, method="average", metric="seuclidean", optimal_ordering=True)

# Output newick tree and save to image
tree = hc.to_tree(linkage)
if isinstance(tree, ClusterNode):
    output_file = f"{args.output}.nwk"
    with open(output_file, "w") as f:
        newick_tree = convert_scipy_to_newick(tree, tree.dist, list(df.columns))
        f.write(newick_tree)
    with open(output_file, "r") as f:
        image_tree = Phylo.read(output_file, "newick")
        image_tree.root_at_midpoint()
        fig = plt.figure(figsize=(10, 20), dpi=300)
        axes = fig.add_subplot(1, 1, 1)
        Phylo.draw(image_tree, axes=axes)
        plt.show()
        plt.savefig(f"{args.output}.png")
