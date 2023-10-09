def RNA(DNA):
    Table = DNA.maketrans({'G': 'C', 'C': 'G', 'T': 'A', 'A': 'T'})
    return DNA.translate(Table)


print(RNA('GGCTAA'))