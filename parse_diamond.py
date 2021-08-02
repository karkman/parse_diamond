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

INFILE = open(args.infile, 'r')
DELIM = args.delimiter

sample_names = []
genes = []

for line in INFILE:
	line = line.rstrip()
	line = line.split("\t")
	sample_names.append(line[0].split(DELIM)[0])
	genes.append(line[1])

cols = set(sample_names)
rows = set(genes)

df = pd.DataFrame(index=rows,columns=cols)
df[:] = 0
print("Matrix created, starting annotation...")

INFILE.close()

INFILE = open(args.infile, 'r')

for line in INFILE:
	 line = line.rstrip()
	 line = line.split("\t")
	 sample = line[0].split(DELIM)[0]
	 gene = line[1]
	 df[sample][gene] = df[sample][gene]+1

INFILE.close()

print("Annotation done, writing outfile...")
df.to_csv(args.outfile, sep=";")
