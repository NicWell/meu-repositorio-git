while True:
    print("="*90, "\n")
    print("Escolha a operação Básica a ser Realizada digitando o respectivo número \n")
    print("\n 1: Soma \n", "2: Subtração \n", "3: Multiplicação \n", "4: Divisão \n", "0: Sair \n")
    operacao = int(input(":"))
    if(operacao == 0):
        print("="*90, "\n")
        break
    if(operacao == 1):
        while True:
            print("Você selecionou soma")
            num1 = float(input("Digite o Primeiro Número: "))
            num2 = float(input("Digite o Segundo Número: "))
            soma = num1 + num2
            print("O resultado da Soma é: ", soma)
            opcao = input("Deseja continuar: s/n : ")
            print("="*90, "\n")
            if( opcao == "n" or opcao == "N"):
                break
    if(operacao == 2):
        while True:
            print("Você selecionou Subtração")
            num1 = float(input("Digite o Primeiro Número: "))
            num2 = float(input("Digite o Segundo Número: "))
            sub = num1 - num2
            print("O resultado da Subtração é: ", sub)
            opcao = input("Deseja continuar: s/n : ")
            print("="*90, "\n")
            if( opcao == "n" or opcao == "N"):
                break
    if(operacao == 3):
        while True:
            print("Você selecionou Multiplicação")
            num1 = float(input("Digite o Primeiro Número: "))
            num2 = float(input("Digite o Segundo Número: "))
            mult = num1 * num2
            print("O resultado da Multiplicação é: ", mult)
            opcao = input("Deseja continuar: s/n : ")
            print("="*90, "\n")
            if( opcao == "n" or opcao == "N"):
                break
    if(operacao == 4):
        while True:
            print("Você selecionou Divisão")
            num1 = float(input("Digite o Primeiro Número: "))
            num2 = float(input("Digite o Segundo Número: "))
            while True:
                if(num2 <= 0):
                    print("Impossível dividir por 0 ou inferior a ele")
                    break
                div = num1/num2
                print("O resultado da Divisão é: ", div)       
                break
            opcao = input("Deseja continuar: s/n : ")
            print("="*90, "\n")
            if( opcao == "n" or opcao == "N"):
                    break
    if(operacao < 0 or operacao > 4):
        print("Número Inválido")
        print("="*90)
