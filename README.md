# BactSeq

Short python script to calculate percentages of sequences which begin with a start codon and have Shine-Dalgarno motifs in a fasta file.

## Requirements

The only requirement is python3. Tested witn version v3.6.3.

## Usage

Run the script as follows:

    python3 percentages.py --input <fasta file>

## Testing

A test file, 'test.fasta', is included and should be run as follows:

    python3 percentages.py --input test.fasta

Giving these results:

    Error at line 4: Sequence is shorter than 20bp. Skipped.
    Percent start codons: 66.67%
    Number of Shine-Delgarno sequences: 1
 	     as a % of seq with starts: 25.00%
	     as a % of all seqs: 16.67%



