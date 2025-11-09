import csv

def calcular_aluguel():
    print("🏠 --- SISTEMA DE ORÇAMENTO DE ALUGUEL --- 🏠\n")

    # Tipos de imóveis
    print("Tipos disponíveis:")
    print("1 - Apartamento (R$ 700,00 - 1 quarto)")
    print("2 - Casa (R$ 900,00 - 1 quarto)")
    print("3 - Estúdio (R$ 1200,00)\n")

    tipo = int(input("Escolha o tipo de imóvel (1/2/3): "))

    # Definir valores base
    if tipo == 1:
        nome_tipo = "Apartamento"
        aluguel_base = 700
    elif tipo == 2:
        nome_tipo = "Casa"
        aluguel_base = 900
    elif tipo == 3:
        nome_tipo = "Estúdio"
        aluguel_base = 1200
    else:
        print("Opção inválida!")
        return

    # Número de quartos (apenas para casa e apartamento)
    quartos = 1
    if tipo in [1, 2]:
        quartos = int(input("Quantos quartos? (1 ou 2): "))
        if tipo == 1 and quartos == 2:
            aluguel_base += 200
        elif tipo == 2 and quartos == 2:
            aluguel_base += 250

    # Garagem (casa/apartamento)
    if tipo in [1, 2]:
        garagem = input("Deseja incluir garagem? (s/n): ").lower()
        if garagem == "s":
            aluguel_base += 300

    # Estúdio com vagas extras
    if tipo == 3:
        vagas = int(input("Quantas vagas de estacionamento? (0, 1, 2 ou mais): "))
        if vagas == 2:
            aluguel_base += 250
        elif vagas > 2:
            aluguel_base += 250 + (vagas - 2) * 60

    # Desconto de 5% para apartamento sem crianças
    if tipo == 1:
        criancas = input("Possui crianças? (s/n): ").lower()
        if criancas == "n":
            aluguel_base *= 0.95  # aplica 5% de desconto

    # Valor do contrato imobiliário
    contrato = 2000
    parcelas = 5
    parcela_contrato = contrato / parcelas

    # Mostrar resultado
    print("\n--- RESUMO DO ORÇAMENTO ---")
    print(f"Tipo de imóvel: {nome_tipo}")
    print(f"Valor mensal do aluguel: R$ {aluguel_base:.2f}")
    print(f"Valor do contrato: R$ {contrato:.2f} (em até {parcelas}x de R$ {parcela_contrato:.2f})")

    total = aluguel_base + parcela_contrato
    print(f"Valor total mensal com contrato: R$ {total:.2f}")

    # Geração do arquivo CSV com 12 parcelas mensais
    gerar_csv(aluguel_base, parcela_contrato)

def gerar_csv(aluguel_mensal, parcela_contrato):
    total_mensal = aluguel_mensal + parcela_contrato
    with open("orcamento_12meses.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Mês", "Aluguel (R$)", "Contrato (R$)", "Total Mensal (R$)"])
        for mes in range(1, 13):
            writer.writerow([f"Mês {mes}", f"{aluguel_mensal:.2f}", f"{parcela_contrato:.2f}", f"{total_mensal:.2f}"])

    print("\n📁 Arquivo 'orcamento_12meses.csv' gerado com sucesso!")

# Executar o programa
if __name__ == "__main__":
    calcular_aluguel()
