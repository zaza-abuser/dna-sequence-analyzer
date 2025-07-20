# src/visualization.py

import matplotlib.pyplot as plt
from collections import Counter

def plot_gc_content(gc_percent):
    plt.figure(figsize=(5, 3))
    plt.bar(["GC Content"], [gc_percent], color="teal")
    plt.ylabel("Percentage")
    plt.title("GC Content")
    plt.ylim(0, 100)
    plt.tight_layout()
    plt.show()


def plot_nucleotide_distribution(sequence):
    counts = Counter(sequence)
    nucleotides = ['A', 'T', 'G', 'C']
    values = [counts.get(base, 0) for base in nucleotides]

    plt.figure(figsize=(6, 4))
    plt.bar(nucleotides, values, color="skyblue")
    plt.title("Nucleotide Distribution")
    plt.xlabel("Base")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()


def plot_sequence_length(length):
    plt.figure(figsize=(5, 3))
    plt.bar(["Sequence Length"], [length], color="orchid")
    plt.ylabel("Bases")
    plt.title("Total Sequence Length")
    plt.tight_layout()
    plt.show()
