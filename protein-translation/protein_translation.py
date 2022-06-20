# Translate rna sequences into proteins

codon_protein_dict = {
    ("AUG"): "Methionine",
    ("UUU", "UUC"): "Phenylalanine",
    ("UUA", "UUG"): "Leucine",
    ("UCU", "UCC", "UCA", "UCG"): "Serine",
    ("UAU", "UAC"): "Tyrosine",
    ("UGU", "UGC"): "Cysteine",
    ("UGG"): "Tryptophan",
    ("UAA", "UAG", "UGA"): "STOP"
}

def proteins(strand):
    """
    Get a list of proteins based on the given strand
    
    :param strand: string - a strand which contains rna
    :return: [string] - a list of proteins
    """
    proteinList = []
    # yields the number of proteins in strand
    numberOfCodons = int(len(strand) / 3)
    for i in range(0, numberOfCodons):
        # get the protein
        startingIndex = i * 3
        codon = strand[startingIndex : startingIndex + 3]
        # use the global dictionary to get the translation
        for key in codon_protein_dict.keys():
            if codon in key:
                translation = codon_protein_dict[key]
                if translation == "STOP":
                    return proteinList
                proteinList.append(translation)
    return proteinList