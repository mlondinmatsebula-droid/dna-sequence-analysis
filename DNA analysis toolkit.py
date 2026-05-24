"""
DNA Sequence Analysis Toolkit (Mini Project)

Features:
- Base counting (A, T, C, G)
- GC content calculation
- DNA → RNA transcription
- Reverse complement generation
"""

dna_seq = "ATGCGTGACTGACGTACAGTACACTGGATTTGAGATTACAATCGC"


# -----------------------------
# Base counting
# -----------------------------
a_count = dna_seq.count("A")
t_count = dna_seq.count("T")
c_count = dna_seq.count("C")
g_count = dna_seq.count("G")


def base_counts(seq):
    return {
        "A": seq.count("A"),
        "T": seq.count("T"),
        "C": seq.count("C"),
        "G": seq.count("G"),
    }


# -----------------------------
# GC content
# -----------------------------
def gc_content(seq):
    return (seq.count("G") + seq.count("C")) / len(seq) * 100


# -----------------------------
# Transcription (DNA → RNA)
# -----------------------------
def transcribe(seq):
    return seq.replace("T", "U")


# -----------------------------
# Reverse complement
# -----------------------------
def reverse_complement(seq):
    mapping = str.maketrans("ATCG", "TAGC")
    return seq.translate(mapping)[::-1]


# -----------------------------
# Results
# -----------------------------
rna_seq = transcribe(dna_seq)
rev_comp = reverse_complement(dna_seq)

print("DNA Sequence:", dna_seq)
print("\nBase Counts:")
print(base_counts(dna_seq))

print(f"\nGC Content: {gc_content(dna_seq):.2f}%")

print("\nRNA Sequence:", rna_seq)
print("\nReverse Complement:", rev_comp)