def consumo_total(consumo):
    return sum(consumo)


def sugestoes_economia(consumo, aparelhos):
    sugestoes = []
    for i in range(len(consumo)):
        if consumo[i] > 1.0:  # Consumo acima de 1 kWh considerado alto
            sugestoes.append(f"Tente reduzir o uso do {aparelhos[i]}, pois consome {consumo[i]:.1f} kWh diariamente.")
    return sugestoes


def verifica_energia_renovavel(consumo_total, energia_solar, energia_eolica):
    energia_total = energia_solar + energia_eolica
    if energia_total >= consumo_total:
        return "A energia gerada por fontes renováveis cobre o consumo total da casa."
    else:
        return f"A energia gerada por fontes renováveis não é suficiente para cobrir o consumo total. Faltam {consumo_total - energia_total:.1f} kWh."


def salvar_dados(consumo_total, sugestoes, analise_renovavel):
    with open("dados_consumo.txt", "w") as file:
        file.write(f"Consumo total diário: {consumo_total:.1f} kWh\n\n")
        file.write("Sugestões para reduzir o consumo de energia:\n")
        for sugestao in sugestoes:
            file.write(f"- {sugestao}\n")
        file.write("\nAnálise de energia renovável:\n")
        file.write(analise_renovavel + "\n")


def exibir_tabela(aparelhos, consumo):
    print("\nTabela de Consumo Diário:")    
    print(f"{'Aparelho':<20}{'Consumo (kWh)':>15}")
    print("-" * 35)
    for i in range(len(aparelhos)):
        print(f"{aparelhos[i]:<20}{consumo[i]:>15.1f}")
    print("-" * 35)


def tabela_informativa():
    print("\nTabela Informativa de Consumo Médio Diário (Referencial):")
    aparelhos_ref = [
        "Geladeira", "Ar-condicionado", "Televisão", "Computador", "Máquina de lavar", "Micro-ondas", "Lâmpada LED"
    ]
    consumo_ref = [1.2, 2.5, 0.8, 0.6, 1.0, 0.7, 0.05]
    exibir_tabela(aparelhos_ref, consumo_ref)


# Exibir tabela informativa ao iniciar
tabela_informativa()

# Entrada de dados do usuário com tratamento de exceções
print("\nDigite os aparelhos e seus respectivos consumos diários em kWh.")
print("Quando terminar, digite 'sair' para finalizar a lista.\n")

aparelhos = []
consumo_diario = []

while True:
    try:
        aparelho = input("Nome do aparelho (ou 'sair'): ")
        if aparelho.lower() == 'sair':
            break
        consumo = float(input(f"Consumo diário do {aparelho} (em kWh): "))
        if consumo < 0:
            raise ValueError("O consumo não pode ser negativo.")
        aparelhos.append(aparelho)
        consumo_diario.append(consumo)
    except ValueError as e:
        print(f"Erro: {e}. Tente novamente.")

try:
    energia_solar = float(input("\nDigite a energia solar gerada diariamente (em kWh): "))
    energia_eolica = float(input("Digite a energia eólica gerada diariamente (em kWh): "))
    if energia_solar < 0 or energia_eolica < 0:
        raise ValueError("A energia gerada não pode ser negativa.")
except ValueError as e:
    print(f"Erro: {e}. Finalizando o programa.")
    exit()

# Processamento
total_consumo_diario = consumo_total(consumo_diario)
sugestoes = sugestoes_economia(consumo_diario, aparelhos)
analise_renovavel = verifica_energia_renovavel(total_consumo_diario, energia_solar, energia_eolica)

# Saída
exibir_tabela(aparelhos, consumo_diario)
print(f"\nConsumo total diário: {total_consumo_diario:.1f} kWh")
print("\nSugestões para reduzir o consumo de energia:")
for sugestao in sugestoes:
    print("-", sugestao)

print("\nAnálise de energia renovável:")
print(analise_renovavel)

# Salvar no arquivo
salvar_dados(total_consumo_diario, sugestoes, analise_renovavel)
print("\nOs dados foram salvos no arquivo 'dados_consumo.txt'.")
