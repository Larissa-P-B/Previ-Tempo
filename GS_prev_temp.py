

# consultar previsão do tempo

print(f"""
      1: Região Norte
      2: Região Sul
      3: Região Nordeste
      4: Região Sudeste,
      5: Região Centro-Oeste
      0: Para Sair
""")

while True :
    v = int(input('Qual a sua região: '))
    match v:
        case 0:
            print("Voltando ao Menu")
            break
        case 1:
            print("Região Norte")
            print(f"""
            Região Norte: Clima Alta Úmidade Temperatura Max 33°C Min 25°C
            - 
            Com risco de chuvas fortes em toda região.
            """)

        case  2:
            print("Região Sul")
            print(f"""
            Região Sul: Clima Baixa Úmidade Temperatura Max 25°C Min 13°C
            - 
            Sem risco de chuvas na região,tendência à um pouco de névoa no anoitecer.
            """)
        case  3:
            print("Região Nordeste")
            print(f"""
            Região Nordeste: Clima Baixa Úmidade Temperatura Max 27°C Min 20°C
            - 
            Pequeno risco de chuvas na região,tendência Sol,com chuva de manhã e diminuição de nuvens a tarde.
            """)
        case 4:
            print("Região Sudeste")
            print(f"""
            Região Susdeste: Clima Baixa Úmidade Temperatura Max 23°C Min 12°C
            - 
            Sem risco de chuvas,tendência clima ensolarado,rajas de vento estão a 8km/h.
            """)
        case 5:
            print("Região Centro-Oeste")
            print(f"""
            Região Centro-Oeste: Clima Alta Úmidade Temperatura Max 26°C Min 16°C
            - 
            Sem risco de chuvas,tendência clima predominantimente ensolarado,rajas de vento estão a 23km/h.
            """)
        case _:
            print("Informação Invalida!!! Tente Novamente. ")

'''if v == 1:
    print("Região Norte")
elif v == 2:
    print("Região Sul")
elif v == 3:
    print("Região Nordeste")
elif v == 4:
    print("Região Sudeste")
elif v == 5:
    print("Região Centro-Oeste")
elif v == 0:
    print("Voltando ao Menu")
else:
    print("Informação Invalida!!! Tente Novamente. ")'''




