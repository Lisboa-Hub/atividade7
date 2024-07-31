while True:
    nome = str(input("Informe o seu nome: "))

    x = float(input("Informe o 1° número: "))
    y = float(input("Informe o 2° número: "))

    print(f"{"="*30}LISTA DE OPERAÇÕES{"="*30}\n")
    print("soma")
    print("subtração")
    print("divisão")
    print("multiplicação")

    opcao = input(f"\n{nome} escolha sua opção de cálculo: ").lower()

    match str(opcao):
        case "soma":
            print(x + y)
        case "subtração":
            print(x - y)
        case "divisão":
            print(x / y)
        case "multiplicação":
            print(x * y)
    continuar = input("Deseja continuar? (s/n)").lower()

    if continuar == "s":
        continue
    else:
        break