# Desafio
# Imagine que você trabalha para uma empresa de telecomunicações e é responsável por validar se um número de telefone fornecido pelo cliente está em um formato correto. Para garantir a precisão dos registros, é essencial que os números de telefone estejam no formato padrão. Desenvolva uma função programa que valide se um número de telefone tem o formato correto.
#Formato esperado:
# O formato aceito para números de telefone é: (XX) 9XXXX-XXXX,
# onde X representa um dígito de 0 a 9. Lembre-se de respeitar os espaços entre os números quando preciso.
# Entrada
# Uma string representando o número de telefone.
# Saída
#Uma mensagem indicando se o número de telefone é válido ou inválido.

import re

def validar_numero_telefone(numero):
    # O padrão regex corresponde ao formato (XX) 9XXXX-XXXX
    padrao = r'\(\d{2}\) 9\d{4}-\d{4}'
    
    if re.fullmatch(padrao, numero):
        return "O número de telefone é válido."
    else:
        return "O número de telefone é inválido."

# Testando a função
print(validar_numero_telefone("(11) 91234-5678"))  # Deve retornar: O número de telefone é válido.
print(validar_numero_telefone("(11) 1234-5678"))   # Deve retornar: O número de telefone é inválido.
