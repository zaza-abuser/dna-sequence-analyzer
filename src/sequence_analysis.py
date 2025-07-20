# src/sequence_analysis.py

def gc_content(seq):
    gc_count = seq.count('G') + seq.count('C')
    return round((gc_count / len(seq)) * 100, 2)

def reverse_complement(seq):
    complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return ''.join(complement.get(base, base) for base in reversed(seq))

def transcribe(seq):
    return seq.replace("T", "U")

def find_motifs(seq, motif):
    positions = []
    for i in range(len(seq) - len(motif) + 1):
        if seq[i:i+len(motif)] == motif:
            positions.append(i + 1)  # 1-based index
    return positions

def translate_dna(seq):
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
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'
    }
    protein = ''
    for i in range(0, len(seq) - 2, 3):
        codon = seq[i:i+3]
        protein += codon_table.get(codon, 'X')
    return protein

def find_orfs(seq):
    start_codon = "ATG"
    stop_codons = {"TAA", "TAG", "TGA"}
    orfs = []
    i = 0
    while i < len(seq) - 2:
        codon = seq[i:i+3]
        if codon == start_codon:
            for j in range(i+3, len(seq) - 2, 3):
                if seq[j:j+3] in stop_codons:
                    orfs.append(seq[i:j+3])
                    i = j + 3
                    break
            else:
                i += 3
        else:
            i += 1
    return orfs

def sequence_stats(seq):
    return {
        'Length': len(seq),
        'GC Content (%)': gc_content(seq),
        'Transcription': transcribe(seq),
        'Reverse Complement': reverse_complement(seq),
    }
