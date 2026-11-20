
# create the class
class Sequence:

    # constructor
    def __init__(self, id, seq):
        self._id = id
        self._seq = seq.upper()
        # make a codon table
        bases = "tcag".upper()
        codons = [a + b + c for a in bases for b in bases for c in bases]
        amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
        self._codon_table = dict(zip(codons, amino_acids))

    @property
    def codon_table(self):        # users gets access to codon_table which is a copy
        return self._codon_table  # of the protected _codon_table
    
    # getter and setter for id
    @property
    def id(self):
        return self._id 
    
    # the setter is here as an example
    """
    @id.setter
    def id(self, id):
        self._id = id
    """

    # getter and setter for seq
    @property
    def seq(self):
        return self._seq
    
    # the setter is here as an example
    """
    @seq.setter
    def seq(self, seq):
        self._seq = seq.upper()
    """

    # gc content method
    def calc_gc_content(self, dp=2):
        c_count = self.seq.count('C')
        g_count = self.seq.count('G')
        gc_content = (c_count + g_count) / len(self.seq)
        return round(gc_content, dp)

    # a method to translate the sequence. This should use the seq attribute of this class,
    # translate it to protein, and return the protein sequence as a string.
    def translate_seq(self): # use self instead of seq and codon table
                                        # should I pass the codon_Table dic?
        # this is good practice in the event that your input is NOT hard coded
        # seq = seq.upper() # not needed anymore as done previously
        # create an empty list
        # it's common to use plural names for lists
        codons = []
        str_seq_AA = ''
        # create a range in steps of 3
        for i in range(0, len(self.seq), 3): 
            # the current value of the range is the start
            # the end is i+3
            codon = self.seq[i:i+3]
            if codon in self.codon_table:
                append_AA = self.codon_table[codon]
                # append this to the list          
                str_seq_AA += append_AA
        return str_seq_AA # Amino acid sequence, codon sequence
    
    # Second, a method to return the id and the sequence attributes as a 
    # string in fasta format, ‘>{id}\n{seq}\n’
    def prep_fasta(self):
        fa_output =f'> {self.id}\n{self.seq}\n'
        return fa_output # fasta sequence
    


## this won't work because there is no setter for this function
#seq1.seq = seq1.seq.lower()


class Proteins:
    # do not use sequence
    def __init__(self, id, seq): # you have not declared id, seq as arguments so not here
        # self._filename = filename
        self._id = id
        self._seq = seq.upper()



if __name__ == '__main__':
    # make two instances of this class
    seq1 = Sequence('geneA', 'ATGCATG')
    seq2 = Sequence('geneB', 'ATTTTAGCGAAA')

    # get the gc content for each seq instance
    print(f'The GC content for {seq1.id} is {seq1.calc_gc_content()}')
    print(f'The GC content for {seq2.id} is {seq2.calc_gc_content(3)}')
    print(f'The protein translation of the {seq1.id} sequence {seq1.seq} is: {seq1.translate_seq()}')

    prot1 = Proteins(seq1.id,seq1.translate_seq())