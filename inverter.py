def inverter(s):
    string_invertida = ''
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]
    return string_invertida

entrada = input("Digite uma string para ser invertida: ")

resultado = inverter(entrada)
print("String invertida:", resultado)