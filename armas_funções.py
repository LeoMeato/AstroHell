from PPlay.sprite import *
from math import *

'''
Manual:

o vetor de tiros da bipper é da seguinte forma: [bipper1, bipper2, ... bipperN], e cada tiro é uma lista por si só:
bipperN = [sprite(0), velocidade no eixo x(1), velocidade no eixo y(2)]

o vetor de tiros da amber é da seguinte forma: [amber1, amber2, ... amberN] e cada tiro é uma lista por si só:
amberN =  [sprite(0), velocidade no eixo x(1), velocidade no eixo y(2), dano(3), piercing acumulado(4), atirou? (5)]

'''

# obs: a amber está dando dano ainda na etapa de carregamento, tem que corrigir. E também tá dando erro se encostar.


def tiroBipper(janela, Mouse, john, velTiro, vetBipper, cooldownB):

    '''
    essa função cria um novo projétil bipper, adiciona na lista vetBipper e define suas propriedades
    '''

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

    '''
    essa função cria um novo projétil amber, adiciona na lista vetBipper e define suas propriedades
    '''

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
        vetAmber[-1].append(False)  # atirou?
        amberPode = False
        cooldownA = 20
    return amberPode, cooldownA


def carregaAmber(amberPode, janela, vetAmber, Mouse, john, timerAmber, mouseApertado, velAmber, danoAmber):

    '''
    Essa função controla o comportamento do projetil da amber enquanto ele ainda não foi atirado.
    '''

    if timerAmber < 5:
        vetAmber[-1][3] += janela.delta_time() / 3
    X = Mouse.get_position()[0]
    Y = Mouse.get_position()[1]
    dx = X - john.x - john.width / 2
    dy = Y - john.y - john.height / 2
    dt = abs(dx) + abs(dy)
    vetAmber[-1][1] = dx / dt * velAmber
    vetAmber[-1][2] = dy / dt * velAmber
    angulo = atan2(dy, dx)
    aumentou = False
    if timerAmber >= 5:
        vetAmber[-1][0] = Sprite("amberProjetil-grande.png")
        vetAmber[-1][3] += 0.4
        aumentou = True
    vetAmber[-1][0].set_position(janela.width / 2 - vetAmber[-1][0].width / 2 + 30 * cos(angulo), janela.height / 2 - vetAmber[-1][0].height / 2 + 30 * sin(angulo))
    #vetAmber[-1][0].draw()
    if aumentou:
        timerAmber = 0
    if not Mouse.is_button_pressed(1) and mouseApertado:
        vetAmber[-1][3] += danoAmber
        vetAmber[-1][5] = True
        return True, timerAmber
    else:
        return False, timerAmber


def renderizaAmber(vetAmber, velJohnX, velJohnY, janela):

    '''
    Essa função define o movimeneto dos projeteis amber após serem atirados, mas não são anulados enquanto ainda estão
    na fase de carregamento, para deixar o projetil com efeito de vibração.
    '''

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

    '''
    Essa função define o comportamento dos projeteis bipper após serem criados.
    '''

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


def colisãoDano(inimigo, tiroB, tiroA, danoB):

    '''
    Essa função analisa se houve colisão entre um inimigo e algum dos 2 tipos de tiro(vetores): o tiroB se refere à
    bipper e o tiroA se refere à amber. Se houver, define o que deve acontecer. A variável danoB se refere ao dano da
    bipper.
    '''

    for i in inimigo:
        for j in tiroB:
            if i[0].collided(j[0]):
                i[1] -= danoB
        for j in tiroA:
            if i[0]. collided(j[0]) and j[5]:
                i[1] -= j[3]
                j[4] += 1

        # se houver colisão com a bipper, o tiro some.
        for j in range(len(tiroB)):
            if tiroB[j][0].collided(i[0]):
                tiroB.pop(j)
                break
