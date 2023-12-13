import pandas as pd

df = pd.read_csv('tabela-fipe-historico-precos.csv',index_col=0)

import pandas as pd

def informacoes_descritivas():
    print('---------------------------------------------------------------')
    print('Informações descritivas:')
    print("Quantidade de registros:", len(df))
    print("Quantidade de colunas:", len(df.columns))
    print("Nome e tipo de cada coluna:")
    print(df.dtypes)
    print("Valores máximos, mínimos e médios de cada coluna:")
    print(df[['anoModelo','mesReferencia','anoReferencia']].max())

# def filtrar_registros():
#     coluna = input("Digite o nome da coluna para filtrar: ")
#     operador = input("Digite o operador de comparação (=, >, <, >=, <=): ")
#     valor = input("Digite o valor para comparar: ")

#     filtro = f"{coluna} {operador} {valor}"
#     resultado = df.query(filtro)
#     print(resultado)

# def realizar_agrupamento():
#     coluna_agrupamento = input("Digite o nome da coluna para agrupar: ")
#     funcao_agregacao = input("Digite a função de agregação (max, min, mean, std): ")

#     resultado_agrupamento = df.groupby(coluna_agrupamento).agg({coluna_agrupamento: funcao_agregacao})
#     print(resultado_agrupamento)

# Menu principal
while True:
    print('---------------------------------------------------------------')
    print("\n1. Informações Descritivas")
    print("2. Filtrar Registros")
    print("3. Realizar Agrupamento de Registros")
    print("0. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        informacoes_descritivas()
    # elif escolha == '2':
    #     filtrar_registros()
    # elif escolha == '3':
    #     realizar_agrupamento()

    elif escolha == '0':
        break
    else:
        print("Opção inválida. Tente novamente.")