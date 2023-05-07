# (**) napisz program, który zlicza wszystkie pliki
# we wszystkich podkatalogach, grupując je wg rozszerzenia;
# wynikiem działania programu powinna być tabelka wyglądająca
# np tak : "JPG": 124, "PNG": 34, "EXE": 2, "TXT": 17
import glob
from os import path

szkoleniePython = glob.glob('..\\Programowanie-w-Pythonie-2023\\**', recursive=True)


def policzRozszerzenia(sciezka):
    rozszerzenia = {}
    miejsceWKompie = glob.glob(sciezka + '\\**', recursive=True)
    for item in miejsceWKompie:
        if path.isdir(item) == True:
            continue
        wyrazy = item.split('.')
        ostatni_wyraz = wyrazy[-1]
        ostatni_wyraz = ostatni_wyraz.lower()
        if len(ostatni_wyraz) > 5:
            continue
        if ostatni_wyraz in rozszerzenia.keys():
            rozszerzenia[ostatni_wyraz] += 1
        else:
            rozszerzenia[ostatni_wyraz] = 1
    return rozszerzenia


UsersFolder = policzRozszerzenia('C:\\Users')
print(UsersFolder)

print(UsersFolder['png'])
