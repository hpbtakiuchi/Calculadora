def imprimeMenu():
    print("Opções possíveis:")
    print("1 - Soma")
    print("2 - Subtração")
    print("0 - Sair")

opcao = 99

while opcao != 0:
    opcao = int(input("Digite a opção: "))
    
    if opcao == 1:
        print("Somando ...")
    elif opcao == 2:
        print("Subtraindo ...")
    elif opcao == 0:
        print("Saindo ...")