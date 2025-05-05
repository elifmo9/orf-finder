#This code reads in a file, classfies if it is DNA, RNA or invalid, and finds the first open reading frame (ORF) in the sequence.
#It also finds all ORFs in the sequence and prints them out.

#read in a file and strip it of whitespace
#returns the sequence as a string
def read_dna_sequence(file_path):
    try:
        with open(file_path, 'r') as file:
            sequence = file.read().strip()
        return sequence
    #if the file is not found, print an error message and return None
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    
# Step 1: Check what type of sequence it is
# checks if the sequence is DNA, RNA, or invalid
def classify_sequence(sequence):
    if 'U' in sequence:
        return 'RNA'
    elif any(base not in 'ATGC' for base in sequence):
        return 'Invalid'
    else:
        return 'DNA'

# Step 2: Find the first open reading frame (ORF) and where it starts
# finds the first start codon (ATG) and checks for stop codons (TAA, TAG, TGA)
def find_orf(sequence):
    stop_codons = ['TAA', 'TAG', 'TGA']
    #look for start codon first
    #if there is no start codon, return no start codon and no ORF
    if 'ATG' not in sequence:
        return None, None, None
    #return the index of the first ATG and an empty list
    start_index = sequence.index('ATG')
    #loop through the sequence after the stop codon in steps of 3 to find stop codons
    #codons are 3 bases long, so we step through the sequence in steps of 3
    for i in range(start_index + 3, len(sequence) - 2, 3):
            codon = sequence[i:i+3]
            if codon in stop_codons:
                #stop position is the index of the stop codon + 3 to include the stop codon in the ORF
                stoppos = i+3
                # Return the ORF (from ATG to stop codon, inclusive) and its start position
                orf = sequence[start_index:stoppos]
                return orf, start_index, stoppos

    # returns none if no valid stop codon found in frame
    return None, None, None

# Step 3: Find all ORFs in the DNA sequence
def find_all_orfs(dna_seq):
    dna_length = len(dna_seq)
    stop_codons = ['TAA', 'TAG', 'TGA']
    orf_starts = []
    orf_seqs = []
    seen_orfs = set()  # Track seen sequences so we don't add duplicates

    for i in range(dna_length - 2):
        codon = dna_seq[i:i+3]
        #look for start codon (ATG)
        if codon == 'ATG':
            startpos = i
            #look for stop codon (TAA, TAG, TGA) in the same frame
            for j in range(startpos + 3, dna_length - 2, 3):
                stopcodon = dna_seq[j:j+3]
                #if a stop codon is found, extract the ORF sequence
                if stopcodon in stop_codons:
                    orf_seq = dna_seq[startpos:j+3]
                    if orf_seq not in seen_orfs:
                        seen_orfs.add(orf_seq)
                        orf_starts.append(startpos)
                        orf_seqs.append(orf_seq)

    return orf_starts, orf_seqs

# --- Main Execution ---

# Step 1: Ask user to input the file name
file_path = input("Enter the full path to the DNA sequence file")
dna_seq = read_dna_sequence(file_path)
#early exit if we cant read the file
if dna_seq is None:
    print("No sequence to process.")
    exit()
else: 
    print(dna_seq)


# Step 2: Classify sequence
classification = classify_sequence(dna_seq)
if classification == 'DNA':
    print("This is a DNA sequence. Let's proceed.")
elif classification == 'RNA':
    print("Error: This is an RNA sequence, not a DNA sequence. Exiting program.")
    exit()
else:
    print("Error: This data was of an unexpected type. Exiting program.")
    exit()

# Step 3: Sequence length
dna_length = len(dna_seq)
print(f"The length of this DNA sequence is {dna_length}")


# Step 4: Find first ORF start and stop
orf_seq, start_pos, stoppos = find_orf(dna_seq)

if orf_seq is not None:
    print(f"The first ORF starts at {start_pos} and ends at {stoppos}")
    print(f"The first ORF sequence is {orf_seq}")
else:
    print("There is no open reading frame in this sequence")


# Step 5: Codons in all reading frames
orf_starts, orf_seqs = find_all_orfs(dna_seq)

# Check if any ORFs were found
#if list is empty, print a message
if not orf_starts:
    print("No ORFs found in the sequence.")
else:
    # Now, print out the ORFs and their start positions
    for i in range(len(orf_starts)):
        start = orf_starts[i]
        orf_seq = orf_seqs[i]

        # Print the ORF
        print(f'Potential ORF at {start}, sequence: {orf_seq}')