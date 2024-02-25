# parse_diamond
A simple and ~very~ moderately slow python script to parse DIAMOND blast output into a count table. Updated to work with python3 and uses pandas to create the data frame.  


The fasta headers have to start with the sample name before the seqeunce name and be separated with some delimiter (by default `-`).  
`>SAMPLE1-M01457:76:000000000-BDYH7:1:1101:17200:1346`  
Might work for other blast outputs too, but use at your own risk. 


In the paired-end version, R1 and R2 reads are annotated separately. The script counts the R2 match only if there was no match on the R1 read. Whether you like it or not.

Usage:
```
python parse_diamond.py -i DIAMOND_OUTPUT -o COUNT_TABLE -d "-"
python parse_diamondPE.py -1 R1_OUTPUT -2 R2_OUTPUT -o COUNT_TABLE -d "-"
```
