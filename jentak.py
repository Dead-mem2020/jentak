# Funkce, která přidává prvek do pole a vrací upravené pole
def pridat_do_pole(pole, prvek):
    pole.append(prvek)
    return pole

# Funkce, která odebere prvek z pole a vrací upravené pole
def odebrat_z_pole(pole, prvek):
    if prvek in pole:
        pole.remove(prvek)
    return pole

# Hlavní část programu
def hlavni():
    # Pole pro uložení prvků
    pole = []

    # Vstup od uživatele s přetypováním na integer
    pocet_prvku = int(input("Zadej počet prvků, které chceš přidat do pole: "))

    # Cyklus s pevným počtem opakování
    for i in range(pocet_prvku):
        # Vstup od uživatele a přidání prvku do pole
        prvek = input(f"Zadej prvek {i+1}: ")
        pole = pridat_do_pole(pole, prvek)

    # Výpis aktuálního pole
    print("Pole po přidání prvků:", pole)

    # Práce s podmínkami a logickými funkcemi
    # Cyklus s podmínkou
    while True:
        akce = input("Chceš odebrat prvek z pole? (ano/ne): ").strip().lower()
        if akce == 'ano':
            prvek = input("Zadej prvek, který chceš odebrat: ")
            pole = odebrat_z_pole(pole, prvek)
            print("Pole po odebrání prvku:", pole)
        elif akce == 'ne':
            break
        else:
            print("Neplatná volba. Zadej 'ano' nebo 'ne'.")

    # Práce s různými datovými typy
    integer_cislo = 42
    string_hodnota = "Hello"
    float_cislo = 3.14
    boolean_hodnota = True

    # Výpis různých datových typů
    print("Integer:", integer_cislo)
    print("String:", string_hodnota)
    print("Float:", float_cislo)
    print("Boolean:", boolean_hodnota)

    # Příklad logických podmínek
    if integer_cislo > 40 and boolean_hodnota:
        print("Integer je větší než 40 a boolean je True")
    if integer_cislo < 40 or not boolean_hodnota:
        print("Integer je menší než 40 nebo boolean není True")

# Spuštění hlavní části programu
hlavni()
