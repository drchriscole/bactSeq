#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculate percentages of start codons 

@author: Chris Cole
"""

import argparse
import re

version = '0.1'

def main(infile):
    """Main code block"""
    
    n = 0
    i = 0
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
    
    print("Percent start codons: {:.2%}".format(i/n))
          
        
    
    

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


