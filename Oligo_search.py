"""
Benjamin Adam Catching
August 12, 2016
California Institute of Technology
Rob Phillips Group
Boundaries of Life Initiative
"""

# Function to read file into string
def file_to_string(file_name = ""):
    """Quick function to read FASTA files into strings"""

    f = open(file_name, 'r')
    text = f.readlines()
    f.close()

    whole_text = "".join(text)
    return ''.join(whole_text.split())

# Function to compute hamming distance
def hamming_distance(text1, text2):
    """Takes two k-length pieces of text and compares level of similarity"""

    # Find length of text
    textlen = len(text1)

    # Assign value that will be added to for each miss-match
    value = 0

    # For the range of the text, compare each nucleotide and check for miss-match
    # For each miss match, add one point to the value
    for i in range(textlen):

        # Compare ith point in both texts
        if text1[i] != text2[i]:

            # If both terms are not equal add one to the value of the output
            value += 1
        else:

            # If both terms math the value remains the same
            value = value

    # Output is an integer that represents the hamming distance
    return value

# Function to take the string and break into all possible kmers
def oligo_list(genome, k):
    """Take a genome and a desired oligomer length k, give a list of kmers"""

    # Initialize list
    pattern_list = []

    # Starting at position 0, working through each 200 mer
    for i in range(len(genome) - k + 1):

        # Pick out 200-mer of ith place in lambda phage
        pattern = genome[i:i+k]

        # Put 200-mer in list
        pattern_list.append(pattern)
    return pattern_list

# Find the unique oligomers of list 1
def unique_oligos(list1, list2, thresh):
    """Given a list of two strings, find the unique oligomers within a certain threshold"""
    # The list of 200-mers to send to Steven
    good_phage_olig = []

    # Start with the ith 200mer

    for i in range(len(list1)):

        # Assign the ith pattern as 'pattern'
        pattern = list1[i]
        print(i / len(list1))
        # Deep plunge of every 200 mer in Ecoli
        temp_value = 0
        for j in range(len(list2)):

            temp_hamming = hamming_distance(list1[i], list2[j])

            if temp_hamming > thresh:
                temp_value += 1
                print('Bad oligo')
            print(temp_value)

        if temp_value == 0:
            good_phage_olig.append(pattern)
            print('One good oligomer')

# Determine whether the oligomer used is unique
def unique_oligo(oligo, genome_list, thresh):
    """A k-length oligo is compared against all other kmers in the genome_list"""

    # Length of genome_list
    genlen = len(genome_list)

    # Assign temporary value to test at end
    value = 0

    # Go through entire genome list
    for i in range(genlen):

        # Find Hamming distance between oligo and ith part of genome_list
        temp_hamming = hamming_distance(oligo, genome_list[i])

        # If the two oligos are differ beyond a certain threshold
        if temp_hamming < thresh:

            # Add to temp value
            value += 1
            print(temp_hamming)

    # If the temp value is still 0, the oligomer is unique within the threshold
    if value == 0:
        return 'Unique oligomer'
    else:
        return 'Not a unique oligomer'



lambda_phage = file_to_string(file_name = 'Lambda_Phage.txt')

Ecoli = file_to_string(file_name = 'Ecoli.txt')

# Create a list of lambda phage oligomers
lambda_phage_list = oligo_list(lambda_phage, 20)

# Create a list of ecoli 200mers
ecoli_list = oligo_list(Ecoli, 20)

# Test if a random oligomer is unique
print(len(lambda_phage_list))
print(len(ecoli_list))
'''
print(unique_oligo(ecoli_list[4], lambda_phage_list, 4))
print(unique_oligo(ecoli_list[1200000], lambda_phage_list, 4))
print(unique_oligo(ecoli_list[3600001], lambda_phage_list, 4))
'''

print(unique_oligo(lambda_phage_list[120], ecoli_list, 4))
print(unique_oligo(lambda_phage_list[24000], ecoli_list, 4))
print(unique_oligo(lambda_phage_list[36000], ecoli_list, 4))

f = open('Proof_of_Concept_Oligomers.txt', 'w')

# List of E. coli probes
"""
f.write('E. coli Probes ')
f.write(ecoli_list[4])
f.write(ecoli_list[1200000])
f.write(ecoli_list[3600001])
"""

# List of Lambda Phage probes
f.write('Lambda Phage Probes ')
f.write('\n')
f.write(lambda_phage_list[120])
f.write('\n')
f.write(lambda_phage_list[24000])
f.write('\n')
f.write(lambda_phage_list[36000])


f.close()
