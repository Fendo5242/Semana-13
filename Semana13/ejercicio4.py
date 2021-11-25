def esVocal(vocal):
    return True if vocal in ["a", "e", "i", "o", "u"] else False
vocal = input("Ingrese una vocal: ")
print(esVocal(vocal))
