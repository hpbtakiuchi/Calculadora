from programaSoma import programaSoma

def imprimeMenu():
    print("Opções possíveis:")
    print("1 - Soma")
    print("2 - Subtração")
    print("0 - Sair")

opcao = 99

while opcao != 0:
    opcao = int(input("Digite a opção: "))
    
    n1 = int(input("Digite o número 1: "))
    n2 = int(input("Digite o número 2: "))

    if opcao == 1:
        pSoma = programaSoma()
        print(f"Soma = {pSoma.adicao(n1,n2)}")
    elif opcao == 2:
        print("Subtraindo ...")
    elif opcao == 0:
        print("Saindo ...")