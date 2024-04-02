def contar_caracteres(texto):
    """
    Conta diferentes tipos de caracteres em uma string.
    texto: A string fornecida pelo usuário.
    Returna um dicionário contendo a contagem de diferentes tipos de caracteres na string.
    """
    total_caracteres = len(texto)
    maiusculas = sum(1 for caractere in texto if caractere.isupper())
    minusculas = sum(1 for caractere in texto if caractere.islower())
    numeros = sum(1 for caractere in texto if caractere.isdigit())
    especiais = sum(1 for caractere in texto if not caractere.isalnum() and not caractere.isspace() and not caractere.isdigit())
    espacos = sum(1 for caractere in texto if caractere.isspace())
    
    return {
        'total': total_caracteres,
        'maiusculas': maiusculas,
        'minusculas': minusculas,
        'numeros': numeros,
        'especiais': especiais,
        'espacos': espacos
    }

entrada = input("Digite uma string: ")

resultado = contar_caracteres(entrada)
print("Número total de caracteres:", resultado['total'])
print("Letras maiúsculas:", resultado['maiusculas'])
print("Letras minúsculas:", resultado['minusculas'])
print("Números:", resultado['numeros'])
print("Caracteres especiais:", resultado['especiais'])
print("Espaços em branco:", resultado['espacos'])
