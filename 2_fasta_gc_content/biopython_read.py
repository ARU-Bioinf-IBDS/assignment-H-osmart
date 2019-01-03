"""
example code showing how fasta file can be read using biopython
Require biopython to be installed

See ../.instructions/4_optional_additional_exercises.md
## 4.5 Read FASTA file with biopython rather than DIY code

Produces output:
$ python biopython_read.py
Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG
Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC
Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT
"""
from Bio import SeqIO
with open("rosalind_sample.txt", "rU") as file_handle:
    for record in SeqIO.parse(file_handle, "fasta"):
        print(record.id)
        print(record.seq)
