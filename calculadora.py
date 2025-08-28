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
    try:
        float_a = float(input("Digite o primeiro valor: "))
        float_b = float(input("Digite o segundo valor: "))
        return float_a,float_b
    except ValueError:
        print("Digite apenas números reais.")

while True:
    try:
        menu()
        try:
            seletor = int(input("Digite aqui:"))
        except ValueError:
            print("Digite um valor válido.")
            continue
        match seletor:
            case 1:
                float_a, float_b = receber_valores()
                resultado = soma(float_a,float_b)
                clear()
                print(f"{float_a} + {float_b} = {resultado}")
                input("Pressione enter para continuar.")
            case 2:
                float_a, float_b = receber_valores()
                resultado = sub(float_a,float_b)
                clear()
                print(f"{float_a} - {float_b} = {resultado}")
                input("Pressione enter para continuar.")
            case 3:
                float_a, float_b = receber_valores()
                resultado = mult(float_a,float_b)
                clear()
                print(f"{float_a} x {float_b} = {resultado}")
                input("Pressione enter para continuar.")
            case 4:
                try:
                    float_a, float_b = receber_valores()
                    resultado = divi(float_a,float_b)
                except ZeroDivisionError:
                    print("Divisão por 0 não é aceita!")
                    input("Pressione enter para continuar.")
                    continue 
                clear()
                print(f"{float_a} / {float_b} = {resultado}")
                input("Pressione enter para continuar.")
                continue       
            case 0:
                break 
            case _:
                print("Digite algo válido, no contexto do programa.")
                input("pressione enter para continuar: ")
                continue
    except Exception as e:
        print(f"Erro inesperado {e}")
        input("Pressione enter para continuar...")            