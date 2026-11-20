# copied from Lab6_problem1
class Fasta:

    # constructor
    def __init__(self, filename): # you have not declared id, seq as arguments so not here
        self._filename = filename
        #self._id = id
        #self._seq = seq.upper()


    def readfasta(self):
        secretedGenes = list()
        with open(f'python_lab6/{filename}') as input_file:   
            for line in input_file:
                GeneID= line.rstrip().strip('>')
                # print (f'the gene Id IS {GeneID}') # print does not work within classes?
                seq = input_file.readline()
                seq1 = Sequence(GeneID, seq) # Turn each id and sequence pair into a DNA sequence object
                # translate_seq(seq,codon_table)
                #prot1 = Proteins(seq1.id,seq1.translate_seq()) # do this outside of the for loop to give 
                                                                # your user an opportunity to get whatever they want
                yield seq1 # you need to use a yield instead of a return here
                           # because you are not getting a single sequence.
                           # You want to go through the for iteration and get all of 
                           # the sequences as you are reading through the file with many
                           # sequences. yield gets something and then pauses and waits for 
                           # you to do something 


