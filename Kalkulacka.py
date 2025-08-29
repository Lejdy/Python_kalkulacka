print("Vitaj v tejto kalkulačke!")
def operácia():
    def číslo1():
        while True:
            user_input = input("Zadaj prvé číslo tvojho príkladu: ")
            try:
                num = float(user_input)
                return num
            except ValueError:
                print("Nevieš čítať? Máš zadať číslo!")
    num1 = číslo1()

    def číslo2():
        while True:
            user_input = input("Zadaj druhé číslo tvojho príkladu: ")
            try:
                num = float(user_input)
                return num
            except ValueError:
                print("Nevieš čítať? Máš zadať číslo!")
    num2 = číslo2()

    user_input = input("Zvoľ si operáciu zadaním znaku operácie (+, -, *, /): ")
    a = num1
    b = num2
    if user_input == "+":
        príklad = a + b
        print("Výsledok je", príklad)
    elif user_input == "-":
        príklad = a - b
        print("Výsledok je", príklad)
    elif user_input == "*":
        príklad = a * b
        print("Výsledok je", príklad)
    elif user_input == "/":
        if num2 == 0:
            print("Nulou sa nedá deliť!")
        else:
            príklad = a / b
            print("Výsledok je", príklad)
    else:
        print("Zadal si nesprávny znak operácie, príklad ti tak neviem vypočítať.")
        
operácia()