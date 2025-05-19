# Questão 1
print('Resolução da Questão 1')

setor_elevador = int(input("Digite o número de setores: "))

if setor_elevador <= 0:
    print("Erro: o número de setores deve ser maior que zero.")
else:
    carga_total = 0
    carga_suportada = 1

    while carga_suportada <= setor_elevador:
        termo = (carga_suportada^2) / (carga_suportada + 1)
        carga_total = carga_total + termo
        carga_suportada = carga_suportada + 1
    print(f"A carga total suportada é: {carga_total:.2f}")