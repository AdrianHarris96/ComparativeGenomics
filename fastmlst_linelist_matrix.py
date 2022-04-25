#!/usr/bin/env python3

# Author:  Kenji Nishiura

"""
Takes Sample ID and Strain Type in fastmlst tabular output and joins with
the metadata linelist based on corresponding Sample ID, and adding columns of a
count matrix based on presence/absence of each food.
"""

import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "-l",
    "--linelist",
    metavar="<linelist>",
    help="Filename for tab-separated linelist. Expecting Sample IDs in first column, Location in second column, Date in third column, and associated foods in >=4th column.",
    required=True,
)
parser.add_argument(
    "-m",
    "--mlst",
    metavar="<fastmlst tabular output>",
    help="Filename for fastmlst tabular output",
    required=True,
)
parser.add_argument(
    "-o",
    "--output",
    metavar="<joined csv output>",
    help="Filename for joined comma-separated output",
    required=True,
)
args = parser.parse_args()

MLSTdf = pd.DataFrame(columns=["SampleID", "ST"])

with open(f"{args.mlst}", "r") as f:
    # skip header
    next(f)
    for line in f:
        # only need first and last columns
        SampleID, *_, ST = line.strip().split(",")
        # get rid of file extension
        SampleID = SampleID.split(".")[0]
        if len(ST) < 1:
            ST = "none"
        # append values of SampleID and ST to df
        MLSTdf = MLSTdf.append({"SampleID": SampleID, "ST": ST}, ignore_index=True)

metadf = pd.DataFrame()

with open(f"{args.linelist}", "r") as f:
    # skip header
    next(f)
    food_dict = {}
    for line in f:
        record = line.strip().split("\t")
        # make sure to have the same number of elements to account for different # foods per line
        while len(record) < 7:
            record.append("")
        metadf = metadf.append(
            {
                "SampleID": record[0],
                "State": record[1],
                "Date": record[2],
                "Food1": record[3].title(),  # title() to make first letter capitalized
                "Food2": record[4].title(),
                "Food3": record[5].title(),
                "Food4": record[6].title(),
            },
            ignore_index=True,
        )

# join metadata and MLST using SampleID as a key
mergeddf = pd.merge(metadf, MLSTdf, on="SampleID")

# create a set of all the values in columns Food1, Food2, Food3, Food4 from mergeddf
foodset = set()
for food in ["Food1", "Food2", "Food3", "Food4"]:
    foodset.update(mergeddf[food])

# make a column for every food in foodset and check for occurrences in food1, food2, food3, food4
for food in foodset:
    mergeddf[food] = mergeddf.apply(
        lambda row: row["Food1"] == food
        or row["Food2"] == food
        or row["Food3"] == food
        or row["Food4"] == food,
        axis=1,
    )

# Replace True with the number 1 in mergeddf
mergeddf.replace(True, 1, inplace=True)

# Replace False with the number 0 in mergeddf
mergeddf.replace(False, 0, inplace=True)

# export merged dataframe to csv
mergeddf.to_csv(f"{args.output}", index=False)
