def vypočítaj():
    číslo1 = input("Zadaj prvé číslo: ")
    def prvé_číslo():
        while True:
            try:
                num1 = int(číslo1)
                return num1
            except ValueError:
                print("Nevieš čítať? Máš zadať číslo!")

    znamienka = input ("Zvoľ si operáciu prostredníctvom znakov +, -, *, /: ")
    def operácia():
        while True:
            if znamienka in ["+" or "-" or "*" or "/"]:
                return znamienka
            else:
                print("To akože nevieš čítať? Môžeš zadať iba znaky +, -, *, /.")
    
    číslo2 = input("Zadaj prvé číslo: ")
    def druhé_číslo():
        while True:
            try:
                num2 = int(číslo2)
                return num2
            except ValueError:
                print("Nevieš čítať? Máš zadať číslo!")

    print("Vytaj v tejto úžastnej kalkulačke.")
    prvý_krok = prvé_číslo()
    druhý_krok = operácia()
    tretí_krok = druhé_číslo()
    
    a = prvé_číslo()
    b = druhé_číslo()
    if znamienka == ["+"]:
        v = a + b
        print(v)
    if znamienka == ["-"]:
        x = a - b
        print(x)
    if znamienka == ["*"]:
        y = a * b
        print(y)
    if znamienka == ["/"]:
        z = a / b
        print("z")

štvrtý_krok = vypočítaj()

    