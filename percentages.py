#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculate percentages of start codons 

@author: Chris Cole
"""

import argparse
import re

version = '0.5.1'

def main(infile):
    """Main code block"""
    
    # variables
    n = 0
    i = 0
    sd = 0
    seq = ''
    
    # open file 
    f = open(infile, 'r')
    
    # interate through file line by line
    for line in f:
        if (re.match('>',line)):
            # count the number of fasta entries
            n = n + 1
            seq = ''
        else:
            if (n == 0):
                raise Exception("ERROR - no defline at line 1. Is '{}' a fasta file?".format(infile))
            if (len(seq) > 1):
                # skip multiline fasta entries
                continue
            if (re.match('ATG', line)):
                # count start codons
                i = i + 1
            else:
                try:
                    # search for S-D sequence
                    if (shineDelgarno(line)):
                        sd = sd + 1
                except Exception as e:
                    print("Error at line {}: {}".format(n, e))
            # store sequence for test for multiline entries
            seq = line
                    
    f.close()
    
    print("Percent start codons: {:.2%}".format(i/n))
    print("Number of Shine-Delgarno sequences: {}".format(sd))
    print("\tas a % of all seqs: {:.2%}".format(sd/n))

          
        
def shineDelgarno(seq, n = 20):
    """
    Determine whether there is a Shine-Delgarno sequence within first 20bp
    
    :params seq: input nucleotide sequence
    :params n: first n bases to query (default: 20)
    """
    
    # check seq is long enough
    if (len(seq) < n):
        raise Exception("Sequence is shorter than 20bp. Skipped.")
    
    # grab first n bases of sequence
    subSeq = seq[:n]
    
    # search for S-D sequence
    if (re.search('AGGAGG',subSeq)):
        return(True)
    else:
        return(False)
    

if __name__ == "__main__":
    # create commandline parameters
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-i', '--in', dest='inf', required=True, 
                        help='The input file')
    parser.add_argument('-d', '--debug', action='store_true', default=False,
                        help='Toggle debugging (default: False)')
    parser.add_argument('-v', '--version', action='version', 
                        version='%(prog)s v{}'.format(version))
    
    args = parser.parse_args()
    
    # finished inital checks, run main()
    main(args.inf)


