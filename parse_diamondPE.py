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
parser.add_argument('-d' '--delimiter', default='-', help='Delimiter between the sample name and the sequence header (default "-")')

args = parser.parse_args()

#check that there is no temp_file already present
if os.path.isfile("temp_file"):
	raise Exception("temp_file exists, you might want to rename it")


INFILE1 = args.reads1
TEMP = open("temp_file", 'w')
DELIM = args.d__delimiter

R1_results = []

with open(INFILE1, "r") as infile:
    for line in infile:
        line = line.rstrip()
        R1_results.append(line.split("\t")[0])
        TEMP.write(line+"\n")


#INFILE1.close()
TEMP.close()

INFILE2 = args.reads2
TEMP = open("temp_file", 'a')

with open(INFILE2, "r") as infile:
    for line in infile:
        line = line.rstrip()
        sequence = line.split("\t")[0]
        if sequence in R1_results:
            next
        else:
            TEMP.write(line+"\n")

TEMP.close()
#INFILE2.close()

sample_names = set()
genes = set()

INFILE1 = open("temp_file", 'r')

with open("temp_file", "r") as infile:
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

#INFILE1.close()

with open("temp_file", "r") as infile:
    for line in infile:
        line = line.rstrip()
        line = line.split("\t")
        sample = line[0].split(DELIM)[0]
        gene = line[1]
        old_count = df._get_value(gene, sample)
        new_count = old_count+1
        df._set_value(gene, sample, new_count)

#INFILE1.close()
print("removing temp file")
os.system("rm temp_file")

print("Annotation done, writing outfile...")
df.to_csv(args.outfile, sep=";")
