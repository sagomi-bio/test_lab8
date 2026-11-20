#  Import each class separately. The syntax is from Package.Module import
# className. You will only be able to use classes that you’ve explicitly
# imported.

#from Package.Module import className
from Sequences_class_module import Sequence # removed the package name here because I am executing it within
                                            # /python_lab8/package_utils/
                                            # if I was in /python_lab8/ then I would have to write:
                                            # from package_utils.Sequences_class_module import Sequence

# 2. Import modules from your package. This way you can import all the classes, but
# you need to give the module a name to use in the code. The syntax to import a
# specific module is import Package.Module as name. You can then access
# the classes in that module by using name.className in your code

import package_utils.fasta_class_module as fastaM
# import Package.Module as name if I was executing this file inside


# make two instances of this class
seq1 = Sequence('geneA', 'ATGCATG')
seq2 = Sequence('geneB', 'ATTTTAGCGAAA')

# get the gc content for each seq instance
print(f'The GC content for {seq1.id} is {seq1.calc_gc_content()}')
print(f'The GC content for {seq2.id} is {seq2.calc_gc_content(3)}')
print(f'The protein translation of the {seq1.id} sequence {seq1.seq} is: {seq1.translate_seq()}')

# Not imported Protein class from the Module so it will not work:
    #prot1 = Proteins(seq1.id,seq1.translate_seq())