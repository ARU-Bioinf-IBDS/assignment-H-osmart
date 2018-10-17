#!/usr/bin/env python
"""
Script to allow manual testing of the transcribe_dna_to_rna
function.
"""
import argparse
from transcribe import transcribe_dna_to_rna


def get_dna_sequence_from_command_line():
    """ gets the input DNA sequence from the command line """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('INPUT_DNA_SEQUENCE',
                        help='the DNA sequence to test (must be specified)')
    args = parser.parse_args()
    return args.INPUT_DNA_SEQUENCE


def main():
    """ main function allows you to manually test """
    dna = get_dna_sequence_from_command_line()
    rna = transcribe_dna_to_rna(dna)
    print(rna)

# run the main method if python is run as script
if __name__ == "__main__":
    main()
