#Get the input DNA sequence from the user in variable dna
dna = input('Enter the DNA sequence: ')

#create dna_complement to store the complement and intialize it to blank
dna_complement = ''

#function to get complement of each DNA symbol
def get_complement(nucleotide):


    """ (str) -> str
    returns the nucleotide's complement

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

        if(nucleotide == 'A'):

            return 'T'

        if(nucleotide == 'T'):

            return 'A'

        if(nucleotide == 'C'):

            return 'G'

        if(nucleotide == 'G'):

            return 'C'

#complement each char in the dna string using for loop over the string.
for char in dna:

    dna_complement += get_complement(char)

#print the dna_complement in the shell window
print(dna_complement)
