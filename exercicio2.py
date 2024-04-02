def analisar_frequencia_letras(texto):
    """
    Analisa a frequência de cada letra em um texto.
    texto: O texto fornecido pelo usuário.
    Returna um dicionário contendo a frequência de cada letra no texto.
    """
    frequencia_letras = {}
    for letra in texto:
        if letra.isalpha():
            letra = letra.lower()
            frequencia_letras[letra] = frequencia_letras.get(letra, 0) + 1
    
    return frequencia_letras

def exibir_histograma_frequencia(frequencia_letras):
    """
    Exibe um histograma da frequência de letras.
    frequencia_letras: Um dicionário contendo a frequência de cada letra.
    """
    print("Histograma de Frequência de Letras:")
    for letra, frequencia in frequencia_letras.items():
        print(f"{letra}: {'*' * frequencia}")

texto = input("Digite um texto: ")

frequencia = analisar_frequencia_letras(texto)
exibir_histograma_frequencia(frequencia)
