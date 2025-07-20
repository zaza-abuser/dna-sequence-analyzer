# src/fasta_parser.py

def read_fasta(filepath):
    """Reads a FASTA file and returns the header and sequence."""
    with open(filepath, "r") as file:
        lines = file.readlines()
    if not lines or not lines[0].startswith(">"):
        raise ValueError("Invalid FASTA format. Missing header line.")
    header = lines[0].strip()
    sequence = "".join(line.strip() for line in lines[1:] if line.strip()).upper()
    return header, sequence
