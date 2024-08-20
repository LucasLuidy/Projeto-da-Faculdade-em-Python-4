def calcular_valor_total(maquina, dias):
    return maquina['valorPorDia'] * dias

def buscar_maquina_por_registro(maquinas, registro_buscado):
    for i, maquina in enumerate(maquinas):
        if maquina['registro'] == registro_buscado:
            return i
    return -1

def preencher_dados(num_maquinas):
    maquinas = []
    for i in range(num_maquinas):
        print(f"Informe os dados da máquina {i + 1}:")
        maquina = {}
        maquina['registro'] = int(input("Número de Registro: "))
        maquina['tipo'] = input("Tipo da Máquina: ")
        maquina['modelo'] = input("Modelo da Máquina: ")
        maquina['fabricante'] = input("Fabricante: ")
        maquina['valorPorDia'] = float(input("Valor por dia de aluguel: "))
        maquinas.append(maquina)
    return maquinas

def listar_maquinas_por_tipo(maquinas, tipo_buscado):
    contador_maquinas = 0
    for maquina in maquinas:
        if tipo_buscado == '' or maquina['tipo'] == tipo_buscado:
            print("Registro:", maquina['registro'])
            print("Tipo:", maquina['tipo'])
            print("Modelo:", maquina['modelo'])
            print("Fabricante:", maquina['fabricante'])
            print("Valor por dia de aluguel:", maquina['valorPorDia'])
            print()
            contador_maquinas += 1
    
    if contador_maquinas == 0:
        print("Não há máquinas deste tipo.")

def main():
    opcao = 0
    maquinas = []
    num_maquinas = 0

    while opcao != 4:
        print("\nMenu de Opções:")
        print("1. Informar número de máquinas")
        print("2. Preencher dados das máquinas")
        print("3. Exibir SubMenu")
        print("4. Encerrar o programa")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            num_maquinas = int(input("Informe o número de máquinas: "))
        elif opcao == 2:
            if num_maquinas == 0:
                print("Antes de preencher os dados, informe o número de máquinas.")
            else:
                maquinas = preencher_dados(num_maquinas)
        elif opcao == 3:
            if num_maquinas == 0:
                print("Antes de escolher esta opção, informe o número de máquinas e preencha os dados.")
            else:
                while True:
                    print("\nSubMenu:")
                    print("1. Entrar com um novo conjunto de máquinas")
                    print("2. Listar máquinas de um determinado tipo")
                    print("3. Pesquisar uma máquina pelo registro")
                    print("4. Voltar ao menu principal")
                    opcao_submenu = int(input("Escolha uma opção: "))
                    if opcao_submenu == 1:
                        print("\n--- Entrando com dados de máquinas ---")
                        maquinas = preencher_dados(num_maquinas)
                    elif opcao_submenu == 2:
                        tipo_buscado = input("Informe o tipo de máquina a ser listado (ou deixe em branco para listar todas): ")
                        listar_maquinas_por_tipo(maquinas, tipo_buscado)
                    elif opcao_submenu == 3:
                        registro_buscado = int(input("Informe o número de registro da máquina: "))
                        indice = buscar_maquina_por_registro(maquinas, registro_buscado)
                        if indice != -1:
                            print("Máquina encontrada:")
                            print("Registro:", maquinas[indice]['registro'])
                            print("Tipo:", maquinas[indice]['tipo'])
                            print("Modelo:", maquinas[indice]['modelo'])
                            print("Fabricante:", maquinas[indice]['fabricante'])
                            print("Valor por dia de aluguel:", maquinas[indice]['valorPorDia'])
                            dias = int(input("Informe o número de dias de aluguel: "))
                            valor_total = calcular_valor_total(maquinas[indice], dias)
                            print("Valor total do contrato de aluguel:", valor_total)
                        else:
                            print("Máquina não encontrada.")
                    elif opcao_submenu == 4:
                        print("Voltando ao menu principal.")
                        break
                    else:
                        print("Opção inexistente, digite uma opção válida.")
        elif opcao == 4:
            print("Encerrando o programa.")
        else:
            print("Opção inexistente, digite uma opção válida.")

main()
