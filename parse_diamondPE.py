#!/usr/bin/env python
## Antti Karkman
## University of Gothenburg
## antti.karkman@gmail.com
## 2018

__author__ = "Antti Karkman"
__version__ = "0.1"

import sys
import os.path
import argparse
import pandas as pd

#parse the arguments
parser = argparse.ArgumentParser(description='Parse Diamond R1 & R2 blast outputs to a count table in CSV format')
parser.add_argument('-1','--reads1',  help='Diamond output for R1 reads')
parser.add_argument('-2', '--reads2', help='Diamond output for R2 reads')
parser.add_argument('-o', '--outfile', default='diamond_table.csv', help='Count table')
parser.add.argument('-d' '--delimiter', default='-', help='Delimiter between the sample name and the sequence header (default "-")')

args = parser.parse_args()

#check that there is no temp_file already present
if os.path.isfile("temp_file"):
	raise Exception("temp_file exists, you might want to rename it")


INFILE1 = open(args.reads1, 'r')
TEMP = open("temp_file", 'w')
DELIM = args.delimiter

R1_results = []

for line in INFILE1:
	line = line.rstrip()
	R1_results.append(line.split("\t")[0])
	TEMP.write(line+"\n")


INFILE1.close()
TEMP.close()

INFILE2 = open(args.reads2, 'r')
TEMP = open("temp_file", 'a')

for line in INFILE2:
	line = line.rstrip()
	sequence = line.split("\t")[0]
	if sequence in R1_results:
		next
	else:
		TEMP.write(line+"\n")
TEMP.close()
INFILE2.close()

sample_names = []
genes = []

INFILE1 = open("temp_file", 'r')

for line in INFILE1:
	line = line.rstrip()
	line = line.split("\t")
	sample_names.append(line[0].split(DELIM)[0])
	genes.append(line[1])

cols = set(sample_names)
rows = set(genes)

df = pd.DataFrame(index=rows,columns=cols)
df[:] = 0
print "Matrix created, starting annotation..."

INFILE1.close()

INFILE1 = open("temp_file", 'r')

for line in INFILE1:
	 line = line.rstrip()
	 line = line.split("\t")
	 sample = line[0].split(DELIM)[0]
	 gene = line[1]
	 df[sample][gene] = df[sample][gene]+1

INFILE1.close()
print "removing temp file"
os.system("rm temp_file")

print "Annotation done, writing outfile..."
df.to_csv(args.outfile, sep=";")
