def gc_content(seq):
    if not seq:
        return 0
    gc = seq.count('G') + seq.count('C')
    return (gc / len(seq)) * 100
def gc_content(seq):
    if not seq:
        return 0
    gc = seq.count('G') + seq.count('C')
    return (gc / len(seq)) * 100

def reverse_complement(seq):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement.get(base, 'N') for base in reversed(seq))

def transcribe(seq):
    return seq.replace('T', 'U')

import re
def find_motifs(seq, pattern):
    return [m.start() for m in re.finditer(pattern, seq)]
codon_table = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
}

def translate_dna(seq):
    protein = ''
    for i in range(0, len(seq)-2, 3):
        codon = seq[i:i+3]
        protein += codon_table.get(codon, 'X')  # 'X' = unknown/invalid
    return protein
def find_orfs(sequence):
    start_codon = 'ATG'
    stop_codons = ['TAA', 'TAG', 'TGA']
    orfs = []

    for frame in range(3):  # check all 3 reading frames
        i = frame
        while i < len(sequence) - 2:
            codon = sequence[i:i+3]
            if codon == start_codon:
                for j in range(i + 3, len(sequence) - 2, 3):
                    stop = sequence[j:j+3]
                    if stop in stop_codons:
                        orfs.append(sequence[i:j+3])
                        i = j + 3  # move past this ORF
                        break
                else:
                    i += 3
            else:
                i += 3
    return orfs

