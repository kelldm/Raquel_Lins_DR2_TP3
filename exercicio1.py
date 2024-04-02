def contar_vogais_consoantes(frase):
    """
    Conta o número de vogais e consoantes em uma frase.
    frase: A frase fornecida pelo usuário.
    Returna um dicionário contendo o número de vogais e consoantes na frase.
    """
    vogais = 'aeiouAEIOU'
    vogais_count = len([letra for letra in frase if letra in vogais])
    consoantes_count = len([letra for letra in frase if letra.isalpha() and letra not in vogais])
    
    return {'vogais': vogais_count, 'consoantes': consoantes_count}

frase = input("Digite uma frase: ")
resultado = contar_vogais_consoantes(frase)
print("Número de vogais:", resultado['vogais'])
print("Número de consoantes:", resultado['consoantes'])
