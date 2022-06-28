# Convert dna to rna

def to_rna(dna_strand):
    """
    Given a DNA strand, return its RNA complement
    (per RNA transcription)
    
    :param dna_strand: str - a string representing dna
    :return: str - a string representing rna
    """
    rna = ""
    for char in dna_strand:
        if char == "G":
            rna += "C"
        elif char == "C":
            rna += "G"
        elif char == "T":
            rna += "A"
        elif char == "A":
            rna += "U"
    return rna
