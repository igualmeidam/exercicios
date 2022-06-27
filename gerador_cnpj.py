import re
from random import randint

"""
Para importar: from gerador_cnpj import gera_cnpj
gera_cnpj(x)
"""


# Verifica se é uma sequência e retorna se é uma sequência ou não
def e_sequencia(cnpj):
    sequencia = cnpj[0] * len(cnpj)
    if sequencia == cnpj:
        return print('Seu cpf é uma sequência')
    else:
        return False


# Remove qualquer caractere que não seja 0-9 e retorna o cnpj trabalhado
def remover_caracteres(cnpj):
    cnpj_trabalhado = re.sub(r'[^0-9]', '', cnpj)
    return cnpj_trabalhado


# Faz o calculo dos dois últimos dígitos e retorna o cnpj completo
def calcula_cnpj(cnpj):
    contador1 = 5
    armazena1 = 0
    for i in range(0, len(cnpj[:12])):
        armazena1 += int(cnpj[i]) * contador1
        contador1 -= 1
        if contador1 < 2:
            contador1 += 8
        calculo1 = 11 - (armazena1 % 11)
        if calculo1 > 9:
            digito1 = 0
        else:
            digito1 = calculo1
    contador2 = 6
    armazena2 = 0
    for i in range(0, len(cnpj[:13])):
        armazena2 += int(cnpj[i]) * contador2
        contador2 -= 1
        if contador2 < 2:
            contador2 += 8
        calculo2 = 11 - (armazena2 % 11)
        if calculo2 > 9:
            digito2 = 0
        else:
            digito2 = calculo2
    return f'{cnpj[:-2]}{digito1}{digito2}'


# Faz a validação do cnpj gerado e retorna se é válido ou inválido
def valida_gerado(cnpj):
    cnpj = cnpj
    cnpj_p_verificar = cnpj
    if e_sequencia(cnpj):
        return print('Seu CNPJ é uma sequência.')
    cnpj_completo = calcula_cnpj(cnpj)
    if cnpj_completo == cnpj_p_verificar:
        return print('Válido')
    else:
        return print('Inválido')


# Gera os dois últimos dígitos do cnpj e o retorna
def gera_digito_cnpj(cnpj):
    contador1 = 5
    armazena1 = 0
    for i in range(0, len(cnpj)):
        armazena1 += int(cnpj[i]) * contador1
        contador1 -= 1
        if contador1 < 2:
            contador1 += 8
        calculo1 = 11 - (armazena1 % 11)
        if calculo1 > 9:
            digito1 = 0
        else:
            digito1 = calculo1
    cnpjnovo = f'{cnpj}{digito1}'
    contador2 = 6
    armazena2 = 0
    for i in range(0, len(cnpjnovo)):
        armazena2 += int(cnpjnovo[i]) * contador2
        contador2 -= 1
        if contador2 < 2:
            contador2 += 8
        calculo2 = 11 - (armazena2 % 11)
        if calculo2 > 9:
            digito2 = 0
        else:
            digito2 = calculo2
    return f'{cnpj}{digito1}{digito2}'


# Agregação das funções para gerar o cnpj, e retorna o cnpj gerado formatado
def gera_cnpj(parametro, cnpjrandom=str(randint(10000000, 99999999))):
    if parametro == 1:
        matriz = '0001'
        cnpj = f'{cnpjrandom}{matriz}'
    elif parametro == 2:
        matriz = '0002'
        cnpj = f'{cnpjrandom}{matriz}'
    valida_gerado(gera_digito_cnpj(cnpj))
    cnpj = gera_digito_cnpj(cnpj)
    formatado = f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{matriz}-{cnpj[12:]}'
    return print(formatado)
