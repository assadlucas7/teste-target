"""
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
"""
# String de exemplo (pode ser substituída por qualquer outra entrada)
string_original = "Teste target"

# Inicializa uma string vazia para armazenar o resultado
string_invertida = ""

# Percorre a string original de trás para frente
for i in range(len(string_original) - 1, -1, -1):
    string_invertida += string_original[i]

# Exibe a string invertida
print(f"String original: {string_original}")
print(f"String invertida: {string_invertida}")
