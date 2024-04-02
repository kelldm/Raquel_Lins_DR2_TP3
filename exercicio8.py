def substituir_palavra(texto, palavra_antiga, palavra_nova):
    """
    Substitui todas as ocorrências de uma palavra por outra em um texto.
    texto: O texto fornecido pelo usuário.
    palavra_antiga: A palavra a ser substituída.
    palavra_nova: A palavra para substituir a palavra antiga.
    Returna o texto com todas as ocorrências da palavra antiga substituídas pela palavra nova.
    """
    return texto.replace(palavra_antiga, palavra_nova)

texto = input("Digite um texto: ")
palavra_antiga = input("Digite a palavra a ser substituída: ")
palavra_nova = input("Digite a palavra para substituir: ")

texto_modificado = substituir_palavra(texto, palavra_antiga, palavra_nova)
print("Texto modificado:", texto_modificado)
