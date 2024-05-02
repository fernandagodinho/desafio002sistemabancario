# Módulo 're' que fornece operações com expressões regulares.
import re


# Crie uma função chamada 'validate_numero_telefone' que aceite um argumento 'phone_number':
def validate_numero_telefone(phone_number):
    # Defina um padrão de expressão regular (regex) para validar números de telefone no formato (XX) 9XXXX-XXXX:
    padrao = r'\(d{2}\) 9\d{4} -\d{4}'
    # A função 're.match()' para verifica se o padrão definido corresponde ao número de telefone fornecido.
    # O 're.match()' retorna um objeto 'match' se houver correspondência no início da string, caso contrário, retorna 'None'.
    if re.match(padrao, phone_number):  
        
        # Agora crie um return, para retornar que o número de telefone é válido:
     return "o numero de telefone é valido ."
    # Crie um else e return, caso não o número de telefone seja inválido:
    else:
     return "o numero de telefone é invalido."
    # Testando a função
print(validate_numero_telefone("(11) 91234-5678"))  # Deve retornar: O número de telefone é válido.
print(validate_numero_telefone("(11) 1234-5678"))   # Deve retornar: O número de telefone é inválido.

