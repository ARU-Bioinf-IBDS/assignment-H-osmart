# Instructions: 
#
# write Python to write the label and sequence to a file 'test_out.fasta'
# in a FASTA format
#
# Hint: look at the fileio_in_python.pdf reference card! 
label='Test_fasta_99999'
sequence='CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACT'
file_out = open('test_out.fasta', 'w')
file_out.write('>' + label + '\n')
file_out.write(sequence + '\n')
file_out.close()
