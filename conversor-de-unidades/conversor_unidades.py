"""

Conversor ver. 1.0.0

"""

def converter_temperatura():
    print("\n--- Conversor de Temperatura ---")
    print("1. Celsius -> Fahrenheit")
    print("2. Fahrenheit -> Celsius")
    opcao = input("Escolha a opção: ")

    if opcao == "1":
        c = float(input("Digite a temperatura em °C: "))
        f = (c * 9/5) + 32
        print(f"{c}°C = {f:.2f}°F")
    elif opcao == "2":
        f = float(input("Digite a temperatura em °F: "))
        c = (f - 32) * 5/9
        print(f"{f}°F = {c:.2f}°C")
    else:
        print("Opção inválida!")

def converter_distancia():
    print("\n--- Conversor de Distância ---")
    print("1. Quilômetros -> Milhas")
    print("2. Milhas -> Quilômetros")
    opcao = input("Escolha a opção: ")

    if opcao == "1":
        km = float(input("Digite a distância em km: "))
        mi = km / 1.609
        print(f"{km} km = {mi:.2f} mi")
    elif opcao == "2":
        mi = float(input("Digite a distância em milhas: "))
        km = mi * 1.609
        print(f"{mi} mi = {km:.2f} km")
    else:
        print("Opção inválida!")

def converter_peso():
    print("\n--- Conversor de Peso ---")
    print("1. Quilogramas -> Libras")
    print("2. Libras -> Quilogramas")
    opcao = input("Escolha a opção: ")

    if opcao == "1":
        kg = float(input("Digite o peso em kg: "))
        lb = kg * 2.205
        print(f"{kg} kg = {lb:.2f} lb")
    elif opcao == "2":
        lb = float(input("Digite o peso em libras: "))
        kg = lb / 2.205
        print(f"{lb} lb = {kg:.2f} kg")
    else:
        print("Opção inválida!")

def main():
    while True:
        print("\n=== Conversor de Unidades ===")
        print("1. Temperatura")
        print("2. Distância")
        print("3. Peso")
        print("0. Sair")

        escolha = input("Escolha uma categoria: ")

        if escolha == "1":
            converter_temperatura()
        elif escolha == "2":
            converter_distancia()
        elif escolha == "3":
            converter_peso()
        elif escolha == "0":
            print("Encerrando... até mais! ✨")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()

"""

Conversor ver. 1.0.0

"""