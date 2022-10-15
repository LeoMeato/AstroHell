from PPlay.sprite import *
from math import *


def tiroBipper(janela, Mouse, john, velTiro, vetBipper, cooldownB):
    X = Mouse.get_position()[0]
    Y = Mouse.get_position()[1]
    if Mouse.is_button_pressed(1) and cooldownB <= 0:
        vetBipper.append([])
        dx = X - john.x - john.width / 2
        dy = Y - john.y - john.height / 2
        dt = abs(dx) + abs(dy)
        vetBipper[-1].append(Sprite("projetil_bipper.png"))
        vetBipper[-1][0].set_position(janela.width / 2, janela.height / 2)
        vetBipper[-1].append(dx / dt * velTiro)
        vetBipper[-1].append(dy / dt * velTiro)
        cooldownB = 10
    return cooldownB

def tiroAmber(janela, vetAmber, Mouse, john, velAmber, amberPode, cooldownA):
    X = Mouse.get_position()[0]
    Y = Mouse.get_position()[1]
    if Mouse.is_button_pressed(1) and amberPode:
        vetAmber.append([])
        dx = X - john.x - john.width / 2
        dy = Y - john.y - john.height / 2
        dt = abs(dx) + abs(dy)
        vetAmber[-1].append(Sprite("amberProjetil-pequeno.png"))
        vetAmber[-1][0].set_position(janela.width / 2 - vetAmber[-1][0].width / 2, janela.height / 2 - vetAmber[-1][0].height / 2)
        vetAmber[-1].append(dx / dt * velAmber)
        vetAmber[-1].append(dy / dt * velAmber)
        vetAmber[-1].append(0)  # dano
        vetAmber[-1].append(0)  # piercing acumulado
        amberPode = False
        cooldownA = 20
    return amberPode, cooldownA


def carregaAmber(amberPode, janela, vetAmber, Mouse, john, timerAmber, mouseApertado, velAmber, danoAmber):
    if timerAmber < 7:
        vetAmber[-1][3] += janela.delta_time() / 5
    X = Mouse.get_position()[0]
    Y = Mouse.get_position()[1]
    dx = X - john.x - john.width / 2
    dy = Y - john.y - john.height / 2
    dt = abs(dx) + abs(dy)
    vetAmber[-1][1] = dx / dt * velAmber
    vetAmber[-1][2] = dy / dt * velAmber
    angulo = atan2(dy, dx)
    aumentou = False
    if timerAmber >= 7:
        vetAmber[-1][0] = Sprite("amberProjetil-grande.png")
        vetAmber[-1][3] += 0.3
        aumentou = True
    vetAmber[-1][0].set_position(janela.width / 2 - vetAmber[-1][0].width / 2 + 30 * cos(angulo), janela.height / 2 - vetAmber[-1][0].height / 2 + 30 * sin(angulo))
    #vetAmber[-1][0].draw()
    if aumentou:
        timerAmber = 0
    if not Mouse.is_button_pressed(1) and mouseApertado:
        vetAmber[-1][3] += danoAmber
        return True, timerAmber
    else:
        return False, timerAmber


def renderizaAmber(vetAmber, velJohnX, velJohnY, janela):
    for i in range(len(vetAmber)):
        vetAmber[i][0].x += (vetAmber[i][1] + velJohnX) * janela.delta_time()
        vetAmber[i][0].y += (vetAmber[i][2] + velJohnY) * janela.delta_time()
        vetAmber[i][0].draw()

    for i in range(len(vetAmber)):
        if vetAmber[i][0].x < 0 or vetAmber[i][0].x > janela.width or vetAmber[i][0].y < 0 or vetAmber[i][
            0].y > janela.height or vetAmber[i][4] > 50:
            vetAmber.pop(i)
            break


def renderizarBipper(vetBipper, janela, velJohnX, velJohnY):
    for i in range(len(vetBipper)):
        vetBipper[i][0].x += (vetBipper[i][1] + velJohnX) * janela.delta_time()
        vetBipper[i][0].y += (vetBipper[i][2] + velJohnY) * janela.delta_time()
        vetBipper[i][0].draw()

    i = 0
    a = len(vetBipper)
    while i < a and a > 0:
        if vetBipper[i][0].x < 0 or vetBipper[i][0].x > janela.width or vetBipper[i][0].y < 0 or vetBipper[i][
            0].y > janela.height:
            vetBipper.pop(i)
            a -= 1
        i += 1


def colisãoDano(inimigo, tiro, tiro2, dano):
    for i in inimigo:
        for j in tiro:
            if i[0].collided(j[0]):
                i[1] -= dano
        for j in tiro2:
            if i[0]. collided(j[0]):
                i[1] -= j[3]
                j[4] += 1
        j = 0
        a = len(tiro)
        while j < a and a > 0:
            if tiro[j][0].collided(i[0]):
                tiro.pop(j)
                a -= 1
            j += 1