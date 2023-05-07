# (*) policz, ile plików o rozszerzeniu ".jpg" jest we wszystkich
# podkatalogach
import glob
from os import listdir, path

pliki = listdir()


def policz_pliki(sciezka='.', rozszerzenie='.txt'):
    if type(sciezka) != str:
        raise ValueError('Podaj sciezka jako str')
    if type(rozszerzenie) != str:
        raise ValueError('Podaj rozszerzenie jako str')
    counter = 0
    pliki = listdir(sciezka)
    for plik in pliki:
        if plik[-(len(rozszerzenie)):] == rozszerzenie:
            counter += 1
    return counter


print(policz_pliki('.'))

szkoleniePython = glob.glob('..\\Programowanie-w-Pythonie-2023\\**', recursive=True)

# z uzyżyciem zdefiniowanej funkcji policz_pliki
licz = 0
for item in szkoleniePython:
    if path.isdir(item) == True:
        licz += policz_pliki(item, '.py')
print(f'tutaj z funkcji policz_pliki: {licz}')

# z wykorzystaniem szalonego glob.glob
licznik = 0
for item in szkoleniePython:
    if item[-3:] == '.py':
        licznik += 1
print(f'tutaj z glob.glob: {licznik}')
