# instructions: write python to write 
# the label and sequence to a file 'test_out.fasta'
# in a FASTA format
label='Test_fasta_99999'
sequence='CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACT'
with open('test_out.fasta', mode='w') as file_out:
    #file_out.write('>' + label + '\n')
    #file_out.write(sequence + '\n')
    print('>' + label, file=file_out)
    print(sequence, file=file_out)

