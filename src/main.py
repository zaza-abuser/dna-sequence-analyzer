# src/main.py

from fasta_parser import read_fasta
from sequence_analysis import (
    gc_content,
    reverse_complement,
    transcribe,
    translate_dna,
    find_motifs,
    find_orfs,
    sequence_stats
)

FASTA_PATH = "../data/test.fasta"

try:
    header, sequence = read_fasta(FASTA_PATH)
except Exception as e:
    print(f"Error reading FASTA file: {e}")
    exit(1)

print(f"\n--- DNA Sequence Analyzer ---")
print(f"Header: {header}")
print(f"Sequence: {sequence}\n")

print("--- Basic Stats ---")
stats = sequence_stats(sequence)
for key, value in stats.items():
    print(f"{key}: {value}")

print("\n--- GC Content ---")
print(f"GC Content: {gc_content(sequence):.2f}%")

print("\n--- Reverse Complement ---")
print(reverse_complement(sequence))

print("\n--- Transcription ---")
print(transcribe(sequence))

print("\n--- Translation (Protein) ---")
print(translate_dna(sequence))

print("\n--- Motif Search: 'ATG' ---")
motifs = find_motifs(sequence, "ATG")
if motifs:
    print(f"Found at positions: {motifs}")
else:
    print("Motif not found.")

print("\n--- Open Reading Frames (ORFs) ---")
orfs = find_orfs(sequence)
if orfs:
    print(f"Found {len(orfs)} ORF(s):")
    for i, orf in enumerate(orfs, 1):
        print(f"ORF {i}: {orf}")
else:
    print("No ORFs found.")
