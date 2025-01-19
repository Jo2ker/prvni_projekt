"""
projekt_1.py: první projekt do Engeto Online Python Akademie

autor: Tomáš Snětivý
email: jo2ker@seznam.cz
"""
# proměnná TEXTS

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# slovník reg_users

reg_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# přihlašovací jméno a heslo

jmeno = input("Zadejte uživatelské jméno: ")
heslo = input("Zadejte heslo: ")

# oddělovací linka

linka = ("-" * 50)
print(linka)

# ověření uživatelského jména a hesla

if jmeno in reg_users and reg_users[jmeno] == heslo:
    print(f"Vítej v aplikaci", jmeno, ", máme tři texty k analýze.")
    print(linka)
else:
    print("Neregistrovaný uživatel, ukončuji program...")
    exit()

# uživatelský vstup pro výběr indexu

vybrany_index = input("Vyber číslo textu od 1 do 3, který chceš analyzovat: ")

# kontrola platnosti indexu a zda je vstup číslo

if vybrany_index.isdigit():
    vybrany_index = int(vybrany_index) - 1
    if vybrany_index < 0 or vybrany_index >= len(TEXTS):
        print("Vybrané číslo není v zadaní, ukončuji program.")
        exit()
    else:
        print(linka)
else:
    print("Zadaný vstup je neplatný, ukončuji program.")
    exit()

# počet slov v textu

slova = TEXTS[vybrany_index].strip().split()
pocet_slov = len(slova)
print("Vybraný text obsahuje", pocet_slov, "slov.")

# počet slov začínajících velkým písmenem

velky_pismeno = [_ for _ in slova if _[0].isupper()]
pocet_velky_pismeno = len(velky_pismeno)
print("Z toho", pocet_velky_pismeno, "slov, začínajících velkým písmenem.")

# počet slov psaných velkými písmeny

velka_pismena = [_ for _ in slova if _.isupper() and _.isalpha()]
pocet_velka_pismena = len(velka_pismena)
print(pocet_velka_pismena, "slov psaných velkými písmeny.")

# počet slov psaných malými písmeny

mala_pismena = [_ for _ in slova if _.islower()]
pocet_mala_pismena = len(mala_pismena)
print(pocet_mala_pismena, "slov psaných malými písmeny.")

# počet čísel

cisla = [int(_) for _ in slova if _.isdigit()]
pocet_cisel = len(cisla)
print("Obsahuje", pocet_cisel, "číselné řetězce.")

# suma všech čísel v textu

soucet = sum(cisla)
print("Součet všech čísel v textu je", soucet)
print(linka)

# výpis hlavičky grafu

print("DÉLKA|       VÝSKYT       |POČET")
print(linka)

# Vytvoření seznamu délek a četnosti slov

delka_slov = []
cetnost_delky = []

for _ in slova:
    delka = len(_.strip('.,!?\''))
    delka_slov.append(delka)

for delka in delka_slov:
    index = delka - 1
    while len(cetnost_delky) <= index:
        cetnost_delky.append(0)
    cetnost_delky[index] += 1

# výpis výsledků

for i in range(len(cetnost_delky)):
    if cetnost_delky[i] > 0:
        print(f" {i + 1:>4}|{"*" * cetnost_delky[i]:<20}|{cetnost_delky[i]}")
exit()