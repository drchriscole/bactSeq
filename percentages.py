#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculate percentages of start codons 

@author: Chris Cole
"""

import argparse
import re

version = '0.2'

def main(infile):
    """Main code block"""
    
    n = 0
    i = 0
    sd = 0
    seq = ''
    f = open(infile, 'r')
    for line in f:
        if (re.match('>',line)):
            n = n + 1
            seq = ''
        else:
            if (len(seq) > 1):
                pass
            if (re.match('ATG', line)):
                i = i + 1
                try:
                    if (shineDelgarno(line)):
                        sd = sd + 1
                except Exception as e:
                    print("Error at line {}: {}".format(n, e))
    
    print("Percent start codons: {:.2%}".format(i/n))
    print("Number of Shine-Delgarno sequences: {}".format(sd))
    print("\tas a % of seq with starts: {:.2%}".format(sd/i))
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


