import re

def validar_senha(senha):
    """
    Valida a senha com base em critérios de complexidade.
    senha: A senha fornecida pelo usuário.
    retorna true se a senha atender aos critérios de complexidade, False caso contrário.
    """
    #Critérios
    comprimento_minimo = 8
    possui_maiuscula = bool(re.search(r'[A-Z]', senha))
    possui_minuscula = bool(re.search(r'[a-z]', senha))
    possui_numero = bool(re.search(r'\d', senha))
    possui_simbolo = bool(re.search(r'[!@#$%^&*()_+=-]', senha))
    
    return (
        len(senha) >= comprimento_minimo and
        possui_maiuscula and
        possui_minuscula and
        possui_numero and
        possui_simbolo
    )

def classificar_complexidade(senha):
    """
    Classifica a complexidade da senha.
    senha: A senha fornecida pelo usuário.
    Returna uma string indicando a complexidade da senha.
    """
    if validar_senha(senha):
        return "Senha forte"
    elif len(senha) >= 6:
        return "Senha média"
    else:
        return "Senha fraca"

senha = input("Digite sua senha: ")

complexidade = classificar_complexidade(senha)
print("Complexidade da senha:", complexidade)
