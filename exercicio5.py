def romano_para_decimal(romano):
    """
    Converte um número romano para decimal.
    romano: O número romano a ser convertido.
    Returna o número decimal correspondente ao número romano.
    """
    romano_decimal = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decimal = 0
    anterior = 0
    for letra in reversed(romano):
        valor = romano_decimal[letra]
        if valor < anterior:
            decimal -= valor
        else:
            decimal += valor
        anterior = valor
    return decimal

def decimal_para_romano(decimal):
    """
    Converte um número decimal para romano.
    decimal: O número decimal a ser convertido.
    Returna o número romano correspondente ao número decimal.
    """
    decimal_romano = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    romano = ''
    for valor, letra in sorted(decimal_romano.items(), reverse=True):
        while decimal >= valor:
            romano += letra
            decimal -= valor
    return romano

entrada = input("Digite um número romano ou decimal: ")

if entrada.isdigit():
    decimal = int(entrada)
    romano = decimal_para_romano(decimal)
    print("Número romano correspondente:", romano)
else:
    romano = entrada.upper()
    decimal = romano_para_decimal(romano)
    print("Número decimal correspondente:", decimal)
