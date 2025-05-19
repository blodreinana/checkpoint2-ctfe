# Questão 3
print('Resolução da Questão 3')

codigo_elevador = int(input("Digite o código do elevador: "))
codigo = codigo_elevador
cubo_digitos = 0
while codigo > 0:
    digito = codigo % 10
    cubo_digitos += digito ** 3
    codigo //= 10

if cubo_digitos % 2 == 0:
    estado = "Normal"
else:
    estado = "Alerta"

print(f"O elevador {codigo_elevador} está em estado: {estado}.")