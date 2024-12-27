def cpf_invalido(cpf):
    return len(cpf) != 11

def nome_invalido(nome):
    return not nome.isalpha()

def numero_celular_invalido(numero_celular):
    return len(numero_celular) != 13