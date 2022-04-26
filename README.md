# Team2-ComparativeGenomics

## FastANI - Whole Genome Approach

FastANI is developed for fast alignment-free computation of whole-genome Average Nucleotide Identity (ANI). ANI is defined as mean nucleotide identity of orthologous gene pairs shared between two microbial genomes. FastANI supports pairwise comparison of both complete and draft genome assemblies. FastANI doesn't require alignments thus its 3 times faster than traditional alignment based ANI methods.

#### Installation

```
conda install -c bioconda fastani

```

#### Usage

The input files in the --ql and --rl options is a text document containing the paths to all the isolates and both the options will be supplied with the same text document.

```
fastani --ql <text-file-containing-paths-to-isolates> --rl <text-file-containing-paths-to-isolates> -o <output_file.out>
./fastani.py -i input_directory
```

This will generate an output_file.out file that contains a tab separated ANI result of a pairwise comparison of all the isolates provided in the input text file. 

## AMRFinder Wrapper

#### Installation

```
conda install -c bioconda ncbi-amrfinderplus
```

#### Usage

```
./amr-finder-wrapper.py -i input_directory -o organism
```

## fastmlst.py
#### Installation

```
conda install fastmlst mafft trimal fasttree
```

#### Usage

Takes in genome assemblies as input, identifies E. Coli 7-site MLST profile, and outputs an approximately-maximum-likelihood phylogenetic tree
```
fastmlst.py [-h] [-c CPUS] -f <fasta input> -o <fasta output> -t <tabular output> -z <tree output>
```

## fastmlst_linelist_matrix.py
#### Dependencies
```
pandas
```

#### Usage

Takes Sample ID and Strain Type in fastmlst tabular output and joins with the metadata linelist based on corresponding Sample ID, and adding columns of a count matrix based on presence/absence of each food.
```
fastmlst_linelist_matrix.py [-h] -l <linelist> -m <fastmlst tabular output> -o <joined csv output>
```

## fastani_vis.py
#### Dependencies
```
pandas
scipy
biopython
matplotlib
```

#### Usage

Takes the tabular output from fastANI and generates a UPGMA tree .nwk and .png file. 
```
fastani_vis.py [-h] -i <input fastani matrix> -o <output prefix>
```
