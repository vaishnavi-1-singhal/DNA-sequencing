def is_valid_dna(sequence):
    sequence = sequence.upper()
    for base in sequence:
        if base not in 'ACGT':
            return False
    return True
def count_bases(sequence):
    sequence = sequence.upper()
    counts={'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for base in sequence:
        if base in counts:
            counts[base] += 1
    return counts
def gc_content(base_counts):
    gc_count = base_counts['G'] + base_counts['C']
    total_count = sum(base_counts.values())
    if total_count == 0:
        return 0.0
    return (gc_count / total_count) * 100
