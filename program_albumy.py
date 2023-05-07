#!/usr/bin/env python3
def make_album(artist, album_name, liczba_utwrow=None):
    # if liczba_utwrow == None:
    #     album = {'artysta':artist, 'nazwa albumu':album_name}
    # else:
    album = {'artysta':artist,
             'nazwa albumu':album_name,
             'utwory':liczba_utwrow,
             }
    return album

def print_album(lista_albumow):
    print('Wprowadzone albumy:')
    for i, el in enumerate(lista_albumow):
        if el['utwory'] == None:
            print(f"{i + 1}. {el['artysta']} - "
                  f"{el['nazwa albumu']}"
                  )
        else:
            print(f"{i + 1}. {el['artysta']} - "
                  f"{el['nazwa albumu']}, {el['utwory']} utworów"
                  )

lista_albumow = []

print('Cześć! Wpisz informacje o albumie!')
print('Jeśli nie znasz ilości utworów na albumie kliknij Enter żeby pominąć')
print('Jeśli chcesz zakończyć wpisz q')
print()

while True:
    artist = input('Jak nazywa się artysta/zespół? ')
    if artist == "q":
        print_album(lista_albumow)
        break
    album = input('Podaj nazwę albumu:')
    if album == "q":
        print_album(lista_albumow)
        break
    song_no = input('Ile jest utworów? ')
    if song_no == "q":
        print_album(lista_albumow)
        break
    else:
        try:
            song_no = int(song_no)
        except ValueError:
            song_no = input(f"Coś poszło nie tak."
                            f"Podaj liczbę utwotów jako liczbę. ")
            try:
                song_no = int(song_no)
            except ValueError:
                print(f"Pierdol sie! Nie umiesz pisać!")
                song_no = None

    if song_no == '':
        song_no = None

    album_uzytkownika = make_album(artist, album, song_no)
    lista_albumow.append(album_uzytkownika)
    artist, album, number = album_uzytkownika.values()
    if number == None:
        print(f"Płyta {artist} nazywa się {album}.\n")
    else:
        print(f"Płyta {artist} nazywa się {album} i ma {number} utworów.\n")
    print(f"Jeśli masz już dość zabawy wpisz 'q' i naciśnij Enter.\n")