import re


def remover_caracteres(cpf):
    cpf_trabalhado = re.sub(r'[^0-9]', '', cpf)
    return cpf_trabalhado


def valida_cpf(cpf_trabalhado):
    contador = 10
    armazena_soma_digito1 = 0
    cpf_pservalidado = cpf_trabalhado[0:9]
    for numero in cpf_pservalidado:
        armazena_soma_digito1 += int(numero) * contador
        contador -= 1
        calculo1 = 11 - (armazena_soma_digito1 % 11)
        if calculo1 > 9:
            digito1 = 0
        else:
            digito1 = calculo1
    cpf_pservalidado2 = cpf_pservalidado + str(digito1)
    contador2 = 11
    armazena_soma_digito2 = 0
    for numero in cpf_pservalidado2:
        armazena_soma_digito2 += int(numero) * contador2
        contador2 -= 1
        calculo2 = 11 - (armazena_soma_digito2 % 11)
        if calculo2 > 9:
            digito2 = 0
        else:
            digito2 = calculo2
    cpf_calculado = cpf_pservalidado2 + str(digito2)
    if cpf_calculado == cpf_trabalhado:
        return True
    else:
        return False
