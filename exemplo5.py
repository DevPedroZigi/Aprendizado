def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        print("Erro: Divisão por zero não é permitida.")
        return None

def exibir_menu():
    while True:
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Sair")
        opcao = int(input("Escolha uma opção: "))
        if 1 <= opcao <= 4:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            
        if opcao == 1:
            print(f"O resultado da soma é: {somar(a, b)}")
        elif opcao == 2:
            print(f"O resultado da subtração é: {subtrair(a, b)}")
        elif opcao == 3:
            print(f"O resultado da multiplicação é: {multiplicar(a, b)}")
        elif opcao == 4:
            resultado = dividir(a, b)
            print(f"O resultado da divisão é: {resultado}")
        elif opcao == 5:
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")



# programa principal
exibir_menu()
