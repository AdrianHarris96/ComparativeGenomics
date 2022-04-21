# Team2-ComparativeGenomics

## FastANI - Whole Genome Approach

FastANI is developed for fast alignment-free computation of whole-genome Average Nucleotide Identity (ANI). ANI is defined as mean nucleotide identity of orthologous gene pairs shared between two microbial genomes. FastANI supports pairwise comparison of both complete and draft genome assemblies. FastANI doesn't require alignments thus its 3 times faster than traditional alignment based ANI methods.

#### Installation

```
conda install -c bioconda fastani

```

#### Usage

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
