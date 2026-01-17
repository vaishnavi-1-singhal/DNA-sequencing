import sys
from data_utils import is_valid_dna, count_bases, gc_content
if len(sys.argv) < 2:
    print("Usage: python analysis.py <path_to_dna_file>")
    sys.exit(1)

file_path = sys.argv[1]
try:
    with open(file_path, 'r') as file:
        sequence = file.read().strip()
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
    sys.exit(1)
if not is_valid_dna(sequence):
    print("Error: Invalid DNA sequence.")
    sys.exit(1)
else:
    base_counts = count_bases(sequence)
    gc_percentage = gc_content(base_counts)
    print("Base Counts:")
    for base, count in base_counts.items():
        print(f"{base}: {count}")
    print(f"GC Content: {gc_percentage:.2f}%")
