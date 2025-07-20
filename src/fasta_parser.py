def read_fasta(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
        seq = ''.join([line.strip() for line in lines if not line.startswith('>')])
    return seq.upper()
