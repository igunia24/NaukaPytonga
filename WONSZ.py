import pygame, sys, random

if not pygame.font:
    print("Warning, fonts disabled")

pygame.init()                                   # zainicjowanie biblioteki pygame
pygame.font.init()

# ---------- ustawienia gry
WYS, SZER = 500, 900                            # to jest wysokość i szerokośc okna w px
KOLOR_TLA = (110, 187, 20)                      # tło to trójtupla
KOLOR_SNK = (55, 55, 55)                        # kolor wensza
SEGM_SNK = 30                                   # długośc segmentu wensza
SZER_SNK = 10                                   # szerokość wensza
score_font = pygame.font.Font('courbd.ttf', 24)
gameOver_font = pygame.font.Font('courbd.ttf', 52)
resume_font = pygame.font.Font('courbd.ttf', 32)

# ---------- okno gry
oknogry = pygame.display.set_mode((SZER, WYS), 0, 32)
pygame.display.set_caption('WONSZ')             # tytuł okna gry


wonsz = [[300, 300], [300+SEGM_SNK, 300], [300+SEGM_SNK, 300-SEGM_SNK], [300+2*SEGM_SNK, 300-SEGM_SNK]]
cukierki = []

def score():
    score = len(wonsz)-4
    return score

def rysuj_gre():
    """ rysowanie obiektów"""
    oknogry.fill(KOLOR_TLA)                     # ---------- tlo rysujemy najpierw
    pygame.draw.lines(oknogry, KOLOR_SNK, False, wonsz, width=SZER_SNK)
    for x, y in wonsz:                          # wyrównanie brzegów węża kołkiem
        pygame.draw.circle(oknogry, KOLOR_SNK, (x+1, y+1), SZER_SNK/2)
    for x, y in cukierki:                       # cukierki dla węża jaki kółka
        pygame.draw.circle(oknogry, KOLOR_SNK, (x+1, y+1), SZER_SNK/2)
    score_text = score_font.render(f'Score: {score()}', True, (KOLOR_SNK))
    oknogry.blit(score_text, (SZER-150, WYS-480))

def rysyj_cukierek(prob, max_cukierki):
    """rysowanie cukierka do zjedzenia dla wensza"""
    los = random.random()
    if los < prob and len(cukierki) < max_cukierki:
        nx = int(SZER / SEGM_SNK) - 1
        ny = int(WYS / SEGM_SNK) - 1
        x = random.randint(1, nx) * SEGM_SNK
        y = random.randint(1, ny) * SEGM_SNK
        cukierki.append((x, y))


def zjadanie_cukierka():
    """jak wonsz zjada cukierka"""
    px, py = wonsz[-1]
    cuk = 0
    for x, y in cukierki:
        if x == px and y == py:
            print('mniam mniam')
            cukierki.pop(cuk)
            ppx, ppy = wonsz[-2]
            wonsz.append([px+px-ppx, py+py-ppy])
        cuk += 1


def game_over_screen():
    """ekran koniec gry"""
    oknogry.fill(KOLOR_TLA)
    text = gameOver_font.render("GAME OVER", True, (10, 10, 10))
    textpos = text.get_rect(centerx=oknogry.get_width() / 2, y=140)
    oknogry.blit(text, textpos)
    text2 = resume_font.render("Naciśij SPACJĘ, aby rozpocząć ponownie", True, (10, 10, 10))
    textpos = text2.get_rect(centerx=oknogry.get_width() / 2, y=200)
    oknogry.blit(text2, textpos)


def poza_plansza():
    x, y = wonsz[-1]
    if x >= SZER-1 or x <= 0+1 or y >= WYS or y <= 0:
        return True
    else:
        return False


def autozjedzenie():
    pozx, pozy = wonsz[-1]
    for x, y in wonsz[:-1]:
        if pozx == x and pozy == y:
            return True


# pętla główna gry
geme_over = False
while True:
    # obsługa zdarzeń generowanych przez gracza
    for event in pygame.event.get():
        if event.type == pygame.QUIT:           # zamykanie gry
            pygame.quit()
            sys.exit()


    if poza_plansza():
        geme_over = True
    if autozjedzenie():
        geme_over = True

    if geme_over == True:
        game_over_screen()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        sys.exit(0)

    if keys[pygame.K_SPACE] and geme_over:
        wonsz = [[300, 300], [300 + SEGM_SNK, 300], [300 + SEGM_SNK, 300 - SEGM_SNK],
                 [300 + 2 * SEGM_SNK, 300 - SEGM_SNK]]
        cukierki = []
        geme_over = False

    if geme_over == False:
        if keys[pygame.K_LEFT]:
            wonsz.pop(0)
            nowy_x = wonsz[-1][0] - SEGM_SNK
            nowy_y = wonsz[-1][1]
            wonsz.append([nowy_x, nowy_y])
        elif keys[pygame.K_RIGHT]:
            wonsz.pop(0)
            nowy_x = wonsz[-1][0] + SEGM_SNK
            nowy_y = wonsz[-1][1]
            wonsz.append([nowy_x, nowy_y])
        elif keys[pygame.K_UP]:
            wonsz.pop(0)
            nowy_x = wonsz[-1][0]
            nowy_y = wonsz[-1][1] - SEGM_SNK
            wonsz.append([nowy_x, nowy_y])
        elif keys[pygame.K_DOWN]:
            wonsz.pop(0)
            nowy_x = wonsz[-1][0]
            nowy_y = wonsz[-1][1] + SEGM_SNK
            wonsz.append([nowy_x, nowy_y])

        rysuj_gre()
        rysyj_cukierek(0.1, 3)
        zjadanie_cukierka()

    pygame.display.flip()
    # odśwież okno i wyświetl
    pygame.display.update()
    pygame.time.delay(100)