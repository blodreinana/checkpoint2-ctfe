# Questão 2
print('Resolução da Questão 2')

def numero_primo(numero):
    if numero <= 1:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
    i = 3
    while i * i <= numero:
        if numero % i == 0:
            return False
        i += 2
    return True

codigo_cabo = int(input("Digite o código do cabo: "))
andar_cabo = int(input("Digite o andar onde o cabo está instalado: "))

soma_digitos = 0
codigo = codigo_cabo
while codigo > 0:
    soma_digitos += codigo % 10
    codigo //= 10
resultado = soma_digitos * andar_cabo

if numero_primo(resultado):
    estado = "PRIMO"
else:
    estado = "NÃO PRIMO"
print(f"O resultado para o cabo {codigo_cabo} no andar {andar_cabo} é {estado}.")

