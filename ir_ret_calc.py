mid_line = "__________"
big_line = "_______________"


def obter_renda():
    while True:
        try:
            r = float(input("Qual o valor da renda?\n").replace(",", "."))
            return r
        except ValueError:
            print("Erro! Escolha um valor válido.")

def vir_calc():
    while True:
        r = obter_renda()

        if r <= 2259.20:
            a = 0
            p = 0
        elif 2259.21 <= r <= 2828.65:
            a = 0.075
            p = 169.44
        elif 2828.66 <= r <= 3751.05:
            a = 0.15
            p = 381.44
        elif 3751.06 <= r <= 4664.68:
            a = 0.225
            p = 662.77
        else:
            a = 0.275
            p = 896.00
        vb = r * a
        vir = vb - p
        print("\n" * 50 + f"{'Renda:':<15}R${r:>10.2f}\n{big_line * 2}\n"
                          f"{'Alíquota:':<15}{a * 100:>10.2f}%\n{big_line * 2}\n"
                          f"{'Valor base:':<15}R${vb:>10.2f}\n{big_line * 2}\n"
                          f"{'Desconto base:':<15}R${p:>10.2f}\n{big_line * 2}\n"
                          f"{'Valor IR retido:':<15}R${vir:>10.2f}\n{big_line * 2}\n")
        while True:
            choice = input("Gostaria de realizar outro cálculo?\n").lower()
            if choice == "sim":
                break

            elif choice in ["não", "nao"]:
                exit()
            else:
                print("Erro! Escolha uma opção válida.")


print("\n" * 2 + f"{mid_line}Calculadora de IR retido na fonte{mid_line}\n")
vir_calc()
