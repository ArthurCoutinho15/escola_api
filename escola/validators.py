import re
from validate_docbr import CPF 

def cpf_invalido(numero_cpf):
    cpf = CPF()
    cpf_valido = cpf.validate(numero_cpf)
    
    return not cpf_valido
    
def nome_invalido(nome):
    return not nome.isalpha()

def numero_celular_invalido(numero_celular):
    # 86 00000-0000
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, numero_celular)
    return not resposta 