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
REGISTROVANI_UZIVATELE = {'USER': 'PASSWORD', 'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}
ODDELOVAC = '-' * 40
POCET_CLANKU = (1, 2, 3)

JMENO = input('username: ')
HESLO = input('password: ')
print(ODDELOVAC)
if REGISTROVANI_UZIVATELE.get(JMENO) == HESLO:
    print('Welcome to the app, ', JMENO, sep='')
    print('We have ', len(POCET_CLANKU), ' texts to be analyzed.', sep='')
    print(ODDELOVAC)
    VYBER = int(input('Enter a number btw. 1 and 3 to select: '))  # Výběr čísla textu

    if VYBER in POCET_CLANKU:
        print(ODDELOVAC)
        TEXT = TEXTS[VYBER - 1]  # Vybraný text
        SLOVA_V_TEXTU = TEXT.split()
        # Výpočet1: počet slov v textu
        POCET_SLOV = len(SLOVA_V_TEXTU)
        print('There are ', POCET_SLOV, ' words in the selected text.', sep='')
        # Výpočet2: počet slov, která začínají na velké písmeno
        SLOVA_1_VELKE = []
        for SLOVO in SLOVA_V_TEXTU:
            for ZNAK in SLOVO:
                if ZNAK.isupper():
                    SLOVA_1_VELKE.append(ZNAK)
                    break
                else:
                    break
        POCET_SLOV_1_VELKE = len(SLOVA_1_VELKE)
        print('There are ', POCET_SLOV_1_VELKE, ' titlecase words.', sep='')
        # Výpočet3: počet slov napsaných velkým písmem
        SLOVA_VELKA = []
        for SLOVO2 in SLOVA_V_TEXTU:
            if SLOVO2.isupper() and SLOVO2.isalpha():
                SLOVA_VELKA.append(SLOVO2)
            else:
                continue
        POCET_SLOV_VELKA = len(SLOVA_VELKA)
        print('There are ', POCET_SLOV_VELKA, ' uppercase words.', sep='')
        # Výpočet4: počet slov napsaných malým písmem
        SLOVA_MALA = []
        for SLOVO3 in SLOVA_V_TEXTU:
            if SLOVO3.islower():
                SLOVA_MALA.append(SLOVO3)
            else:
                continue
        POCET_SLOV_MALA = len(SLOVA_MALA)
        print('There are ', POCET_SLOV_MALA, ' lowercase words.', sep='')
        # Výpočet5: počet čísel
        CISLA = []
        for SLOVO4 in SLOVA_V_TEXTU:
            if SLOVO4.isdecimal():
                CISLA.append(SLOVO4)
            else:
                continue
        POCET_CISEL = len(CISLA)
        print('There are ', POCET_CISEL, ' numeric strings.', sep='')
        # Výpočet6: suma čísel
        CISLA2 = []
        for ZNAK2 in CISLA:
            CISLA2.append(int(ZNAK2))
        SUMA_CISEL = 0
        for ZNAK3 in CISLA2:
            SUMA_CISEL += ZNAK3
        print('The sum of all the numbers ', SUMA_CISEL, sep='')
        print(ODDELOVAC)
        # Výpočet7: četnost délek slov - MÁM ŠPATNĚ!!!!
        DELKA_SLOVA = []
        for SLOVO5 in SLOVA_V_TEXTU:
            DELKA_SLOVA.append(len(SLOVO5))

        CETNOSTI = {}
        for ZNAK4 in DELKA_SLOVA:
            CETNOSTI[str(ZNAK4)] = CETNOSTI.setdefault(str(ZNAK4), 0) + 1

        HODNOTY_CETNOSTI = []
        for ZNAK5 in CETNOSTI.values():
            HODNOTY_CETNOSTI.append(ZNAK5)
        MAX_HODNOTY = max(HODNOTY_CETNOSTI)

        KLICE_CETNOSTI = []
        for ZNAK6 in CETNOSTI.keys():
            KLICE_CETNOSTI.append(int(ZNAK6))
        MAX_KLICE = max(KLICE_CETNOSTI)
        DELKA_MAX_KLICE = len(str(MAX_KLICE))

        print(' LEN| OCCURENCES', ' ' * (MAX_HODNOTY - 10), '|NR.')
        print(ODDELOVAC)
        for KLIC, HODNOTA in CETNOSTI.items():
            print(' ' * (DELKA_MAX_KLICE - len(KLIC)), KLIC, '|', '*' * HODNOTA, ' ' * (MAX_HODNOTY - HODNOTA), '|',
                  HODNOTA)

    else:
        print('Promiň, zadal jsi neexistující číslo textu.')
else:
    print('Promiň, zadal jsi špatnou kombinaci přihlašovacího jména a hesla.')