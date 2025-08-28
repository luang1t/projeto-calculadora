import os

def soma(float_a:float,float_b:float):
    return float_a + float_b
def sub(float_a:float,float_b:float):
    return float_a - float_b
def mult(float_a:float,float_b:float):
    return float_a * float_b
def divi(float_a:float,float_b:float):
    return float_a/float_b
def menu():
    print('='*13, 'MENU CALCULADORA', '='*13)
    print("""1 - SOMA
2 - SUBTRAÇÃO
3 - MULTIPLICAÇÃO
4 - DIVISÂO""")
    print('='*44)
def clear():
    return os.system('cls')
def receber_valores():
    while True:
        try:
            float_a = float(input("Digite o primeiro valor: "))
            float_b = float(input("Digite o segundo valor: "))
            return float_a,float_b
        except ValueError:
            print("Digite apenas números reais.")

while True:
    try:
        clear()
        menu()
        try:
            seletor = int(input("Digite aqui:"))
        except ValueError:
            print("Digite um valor válido.")
            input("Pressione ENTER para continuar...")
            continue
        match seletor:
            case 1:
                float_a, float_b = receber_valores()
                resultado = soma(float_a,float_b)
                clear()
                print(f"{float_a} + {float_b} = {resultado}")
            case 2:
                float_a, float_b = receber_valores()
                resultado = sub(float_a,float_b)
                clear()
                print(f"{float_a} - {float_b} = {resultado}")
            case 3:
                float_a, float_b = receber_valores()
                resultado = mult(float_a,float_b)
                clear()
                print(f"{float_a} x {float_b} = {resultado}")
            case 4:
                float_a, float_b = receber_valores()
                try:                   
                    resultado = divi(float_a,float_b)
                    clear()
                    print(f"{float_a} / {float_b} = {resultado}")
                except ZeroDivisionError:
                    print("Divisão por 0 não é aceita!")       
            case 0:
                break 
            case _:
                print("Opção inválida. Escolha um número entre 0 e 4.")

        input("Pressione ENTER para continuar...")

    except Exception as e:
        print(f"Erro inesperado {e}")
        input("Pressione enter para continuar...")           