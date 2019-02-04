def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len(dna1) > len(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    count = 0
    for char in dna:
        if char == nucleotide:
            count += 1
    return count
        



def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1

def is_valid_sequence(dna):
    """ (str) -> bool

    returns true if the DNA sequence dna is valid.
    
    >>>is_valid_sequence('ATCG')
    True
    >>>is_valid_sequence('adh')
    False

    """
    count = 0
    for char in dna:
        if char not in 'ATCG':
            count =+ 1
    return count == 0

def insert_sequence(dna1,dna2,index):
    """ (str,str,int) -> str

    returns the dna sequence obtained by inserting dna2 into the dna1 at given index.
    
    >>>insert_sequence('CCGG','AT',2)
    CCATGG
    >>>insert_sequence('ATCCG','TT',4)
    ATCCGTT

    """
    return dna1[:index] + dna2 + dna1[index:len(dna1)]
    
def get_complement(nucleotide):
    """ (str) -> str

    returns the nucleotide's complement.
    
    >>>get_complement('A')
    T
    >>>get_complement('T')
    A
    >>>get_complement('C')
    G
    >>>get_complement('G')
    C
    

    """
    if nucleotide in 'ATCG':
        if( nucleotide == 'A'):
            return 'T'
        elif ( nucleotide == 'T'):
            return 'A'
        elif ( nucleotide == 'C'):
            return 'G'
        elif ( nucleotide == 'G'):
            return 'C'
        
    
def get_complementary_sequence(dna):
    """ (str) -> str

    returns the dna sequence's complement.
    
    >>>get_complementary_sequence('ATCG')
    TAGC
    >>>get_complementary_sequence('TGGC')
    ACCG
    """
    comp_seq = ''
    for char in dna:
        comp_seq += get_complement(char)
    return comp_seq
