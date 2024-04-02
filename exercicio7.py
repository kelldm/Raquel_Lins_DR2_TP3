import random
import string

def gerar_senha(comprimento):
    """
    Gera uma senha aleatória com letras (maiúsculas e minúsculas), números e símbolos.
    comprimento: O comprimento da senha a ser gerada.
    Returna a senha aleatória gerada.
    """
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

comprimento = int(input("Digite o comprimento da senha: "))

senha_gerada = gerar_senha(comprimento)
print("Senha gerada:", senha_gerada)
