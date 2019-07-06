def to_rna(dna_strand):
    complements = {'G' : 'C', 'C' : 'G' , 'T' : 'A', 'A' : 'U'}
    rna_strand = ''
    for nucleotide in dna_strand:
        rna_strand += complements[nucleotide]
    return rna_strand
