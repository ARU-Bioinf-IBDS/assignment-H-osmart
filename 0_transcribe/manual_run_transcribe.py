#!/usr/bin/env python
"""
Transcribing DNA into RNA
from http://rosalind.info/problems/rna/
"""
from transcribe import transcribe_dna_to_rna


def main():
    """ main function allows you to manually test """
    dna = input('Enter DNA sequence> ')
    rna = transcribe_dna_to_rna(dna)
    print(' RNA transcription: ' + rna)

# run the main method if python is run as script
if __name__ == "__main__":
    main()
