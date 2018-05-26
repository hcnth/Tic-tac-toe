import random


def generujDna():
    dna = []
    for i in range(10):
        wsp = []
        for j in range(2):
            wsp.append(random.randint(0, 20))
        dna.append(wsp)
    return dna


def obliczWartoscKomorki(wartosc, wsp):
    return wsp[0]*wartosc + wsp[1]


def wyznacznik(plansza):
    return plansza[0]*plansza[4]*plansza[8] + plansza[3]*plansza[7]*plansza[2] + plansza[6]*plansza[1]*plansza[5] - plansza[3]*plansza[1]*plansza[8] - plansza[0]*plansza[7]*plansza[5] - plansza[6]*plansza[4]*plansza[2]


def wybierzRuch(plansza, gracz, dna):
    plansza1 = []
    for i in range(len(plansza)):
        for j in range(len(plansza[i])):
            wartosc = obliczWartoscKomorki(plansza[i][j], dna[i*3+j])
            plansza1.append(wartosc)

    wyzn = (obliczWartoscKomorki(wyznacznik(plansza1), dna[9]) % 9)
    if(wyzn == 0):
        wyzn = 1
    i = 0
    j = 0
    while(True):
        if(plansza[i][j] == 0):
            wyzn -= 1
        if(wyzn == 0):
            return i, j
        j += 1
        if(j > 2):
            j = 0
            i += 1
        if(i > 2):
            i = 0
            j = 0


print(wybierzRuch([[0, 1, -1], [0, 0, 1], [0, 1, -1]], 1, generujDna()))
