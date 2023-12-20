def no_space(texto):
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto

def es_palindromo(texto):
    texto = no_space(texto)
    print(texto)

es_palindromo("Amo la paloma")