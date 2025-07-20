from fasta_parser import read_fasta
from sequence_analysis import (
    gc_content,
    reverse_complement,
    transcribe,
    find_motifs,
    translate_dna,
    find_orfs
)

fasta_file = "../data/test.fasta"
sequence = read_fasta(fasta_file)

print("Loaded Sequence:", sequence)
print("GC Content:", gc_content(sequence))
print("Reverse Complement:", reverse_complement(sequence))
print("Transcription (RNA):", transcribe(sequence))
print("Motif 'ATG' found at positions:", find_motifs(sequence, "ATG"))
print("Protein Translation:", translate_dna(sequence))

orfs = find_orfs(sequence)
print("Found ORFs:")
for i, orf in enumerate(orfs, 1):
    print(f"ORF {i}: {orf}")
orfs = find_orfs(sequence)
print(f"Found {len(orfs)} ORFs:")
for i, orf in enumerate(orfs, 1):
    print(f"ORF {i}: {orf}")
