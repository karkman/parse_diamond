# parse_diamond.py
A simple python script to parse DIAMOND blast output into a count table. Works in python2 and uses pandas to create the data frame.  

The fasta headers have to start with the sample name and be separated with `-`.  
`>SAMPLE1-M01457:76:000000000-BDYH7:1:1101:17200:1346`  
Might work for other blast outputs too, but use at your own risk. 

Usage:  
`python parse_diamond.py -i DIAMOND_OUTPUT -o COUNT_TABLE`
