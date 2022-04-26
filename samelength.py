# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 12:59:29 2022

@author: jaipa
"""


from Bio import SeqIO
from Bio import Seq

def samelength(input_file):
    records = SeqIO.parse(input_file, 'fasta')
    records = list(records) # make a copy, other wise our generator
                        # is exhausted after calculating maxlen
    maxlen = max(len(record.seq) for record in records)

# pad sequences so that they all have the same length
    for record in records:
      if len(record.seq) != maxlen:
        sequence = str(record.seq).ljust(maxlen, '.')
        record.seq = Seq.Seq(sequence)
    assert all(len(record.seq) == maxlen for record in records)

# write to temporary file and do alignment
    output_file = input_file
    with open(output_file, 'w') as f:
        SeqIO.write(records, f, 'fasta')

    