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
conda install fastmlst mafft trimal fasttree pandas dataframe_image
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

## ParSNP 
ParSNP is a command-line-tool that combines aspects from both whole-genome alignment and read mapping to detect SNPs and build phylogenetic trees. 

#### Installation
```
conda install -c bioconda parsnp

OR

wget https://github.com/marbl/parsnp/releases/download/v1.2/parsnp-Linux64-v1.2.tar.gz
tar -xvf parsnp-Linux64-v1.2.tar.gz
```

#### Usage
Takes the reference genome and set of genomes as inputs. Users also have the option to specify the output directory, provide the number of threads, select the use of PhiPack to filter out high recombination regions (optional -x flag), and include all the genomes/isolates in the directory, ignoring the curated genomes according to MUMi (optional -c flag).
```
parsnp -r <reference_fasta> -d <genomes> -o <output_dir> -p <threads> -x -c
```
Output consists of a .ggr file (for gingr visualization), .tree file (in nwk format), and .xmfa file. 

## kSNP 
KSNP is a command-line-tool that identifies SNPs based on k-mer analysis. According to the developers of kSNP, k=19 or k=21 serves as the optimal k for bacteria isolates. 

#### Dependencies
```
tcsh - tcsh can be acquired through two methods:
(1) sudo apt-get install tcsh
(2) conda install -c conda-forge tcsh
```

#### Installation
```
conda install -c hcc ksnp

Proceed with method (1) or method (2):

(1)	Move kSNP to /usr/local
	Open/create the .bash_profile file and paste the text below to add kSNP to your path:
		export PATH="/usr/local/kSNP3:$PATH"

	Open/create the .tcshrc file and paste the text below to add kSNP to the path of your tcsh:
		setenv PATH $PATH\:/usr/local/kSNP3

	Close the terminal window to reset. 

(2)	To install kSNP and/or tcsh elsewhere (besides /usr/local and /bin, respectively), edit the kSNP executable in a text editor:
	Edit the shebang line at top of the file from <#!/bin/tcsh> to <#!/desired_location>
	Edit line near top of the file from <set kSNP=/usr/local/kSNP3> to <set kSNP=/desired_location>
```

#### Usage
Creates a file, entitled "in_list", using the directory of genomes/isolates. After running MapeKSNP3infile, users must provide the output directory and k-mer count. Users have the option to specify the number of CPU cores to use, output the optional neighbor-joining tree (-NJ flag), and output the optional maximum likelihood tree (-ML flag).
```
MakeKSNP3infile <genomes_dir> in_list A
kSNP3 -in in_list -outdir <output_dir> -k <kmer> -CPU <cores> -NJ -ML

```
Output consists of multiple .parsimony (default), .NJ (optional), and .ML (optional) trees. 
