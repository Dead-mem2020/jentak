# Funkce, která přidává prvek do pole a vrací upravené pole
def pridat_do_pole(pole, prvek):
    # Přidání prvku do pole
    pole.append(prvek)
    # Vrácení upraveného pole
    return pole

# Funkce, která odebere prvek z pole a vrací upravené pole
def odebrat_z_pole(pole, prvek):
    # Kontrola, jestli je prvek v poli
    if prvek in pole:
        # Odebrání prvku z pole
        pole.remove(prvek)
    # Vrácení upraveného pole
    return pole

# Hlavní část programu
def hlavni():
    # Inicializace prázdného pole
    pole = []

    # Vstup od uživatele s přetypováním na integer
    pocet_prvku = int(input("Zadej počet prvků, které chceš přidat do pole: "))

    # Cyklus s pevným počtem opakování
    for i in range(pocet_prvku):
        # Vstup od uživatele a přidání prvku do pole
        prvek = input(f"Zadej prvek {i+1} (může být integer, string, float nebo boolean): ")

        # Pokusíme se přetypovat na integer
        # Pokud python nemůže převést prvek na nějaký datový typ, except ValueError to donutí jít na další dat. typ
        try:
            prvek = int(prvek)
        except ValueError:
            # Pokud to není integer, zkusíme float
            try:
                prvek = float(prvek)
            except ValueError:
                # Pokud to není float, zkusíme boolean
                if prvek.lower() == "true":
                    prvek = True
                elif prvek.lower() == "false":
                    prvek = False

        # Přidání prvku do pole
        pole = pridat_do_pole(pole, prvek)

    # Výpis aktuálního pole
    print("Pole po přidání prvků:", pole)

    # Práce s podmínkami a logickými funkcemi
    # Cyklus s podmínkou
    while True:
        akce = input("Chceš odebrat prvek z pole? (ano/ne): ").strip().lower()
        if akce == 'ano':
            prvek = input("Zadej prvek, který chceš odebrat: ")

            # Pokusíme se přetypovat na původní typ
            try:
                prvek = int(prvek)
            # Tohle je to samí, co na lince 31, ale umístěný tak, aby se to lépe přirovnalo
            except ValueError: 
                try:
                    prvek = float(prvek)
                except ValueError:
                    if prvek.lower() == "true":
                        prvek = True
                    elif prvek.lower() == "false":
                        prvek = False

            # Odebrání prvku z pole
            pole = odebrat_z_pole(pole, prvek)
            # Výpis upraveného pole
            print("Pole po odebrání prvku:", pole)
        elif akce == 'ne':
            # Ukončení cyklu, pokud uživatel nechce odebrat další prvky
            break
        else:
            # Neplatná volba, opakování dotazu
            print("Neplatná volba. Zadej 'ano' nebo 'ne'.")

    # Příklad logických podmínek
    integer_cislo = 69
    string_slovo = "Spam <3"
    float_cislo = 0.690420
    boolean_hodnota = True

    # Výpis různých datových typů
    print("Integer:", integer_cislo)
    print("string:", string_slovo)
    print("float:", float_cislo)
    print("Boolean:", boolean_hodnota)

    # Příklad logických podmínek (větší, menší)
    if integer_cislo > 40 and boolean_hodnota:
        print("Integer je větší než 40 a boolean je True")
    if integer_cislo < 40 or not boolean_hodnota:
        print("Integer je menší než 40 nebo boolean není True")

# Spuštění hlavní části programu
hlavni()
