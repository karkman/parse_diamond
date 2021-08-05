#!/usr/bin/env python

import sys
import argparse
import pandas as pd

#parse the arguments
parser = argparse.ArgumentParser(description='Parse Diamond blast output to a count table in CSV format')
parser.add_argument('-i','--infile',  help='Input file from diamond')
parser.add_argument('-o', '--outfile', default='diamond_table.csv', help='Count table')
parser.add_argument('-d', '--delimiter', default='-', help='Delimiter between the sample name and the sequence header (default "-")')
									    
args = parser.parse_args()

INFILE = args.infile
DELIM = args.delimiter

sample_names = set()
genes = set()

with open(INFILE, "r") as infile:
    for line in infile:
        line = line.rstrip()
        line = line.split("\t")
        sample_names.add(line[0].split(DELIM)[0])
        genes.add(line[1])

cols = sorted(sample_names)
rows = sorted(genes)

df = pd.DataFrame(index=rows,columns=cols)
df[:] = 0
print("Matrix created, starting annotation...")

#INFILE.close()
#INFILE = open(args.infile, 'r')

with open(INFILE, "r") as infile:
    for line in infile:
        line = line.rstrip()
        line = line.split("\t")
        sample = line[0].split(DELIM)[0]
        gene = line[1]
        old_count = df._get_value(gene, sample)
        new_count = old_count+1
        df._set_value(gene, sample, new_count)

#INFILE.close()

print("Annotation done, writing outfile...")
df.to_csv(args.outfile, sep=";")

