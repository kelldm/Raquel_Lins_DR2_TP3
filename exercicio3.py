def calcular_media(numeros):
    """
    Calcula a média dos números fornecidos.
    numeros: Uma lista de números.
    Returna a média dos números.
    """
    return sum(numeros) / len(numeros)

def ler_numeros():
    """
    Lê uma sequência de números fornecidos pelo usuário.
    Returna uma lista contendo os números fornecidos.
    """
    entrada = input("Digite uma sequência de números separados por espaço: ")
    numeros_texto = entrada.replace(',', '.').split()  # Substitui vírgulas por pontos e divide a string em uma lista
    numeros = [float(numero) for numero in numeros_texto]
    return numeros

numeros = ler_numeros()
media = calcular_media(numeros)
print("A média dos números é:", media)
