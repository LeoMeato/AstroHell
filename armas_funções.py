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
        vetBipper[-1].append(Sprite("Sprites/projetil_bipper.png"))
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
        vetAmber[-1].append(Sprite("Sprites/amberProjetil-pequeno.png"))
        vetAmber[-1][0].set_position(janela.width / 2 - vetAmber[-1][0].width / 2, janela.height / 2 - vetAmber[-1][0].height / 2)
        vetAmber[-1].append(dx / dt * velAmber)
        vetAmber[-1].append(dy / dt * velAmber)
        vetAmber[-1].append(0)  # dano
        vetAmber[-1].append(0)  # piercing acumulado
        vetAmber[-1].append(False)  # atirou?
        amberPode = False
        cooldownA = 20
    return amberPode, cooldownA


def bumerarma(Bumerarma, janela, Mouse, john, velJohnX, velJohnY, Summon, nivelBumer):

    '''
    essa função controla a arma após ser ativada
    '''

    # controla o comportamento da arma enquanto está em movimento
    if Bumerarma['ativo?']:

        # controla a volta do bumerangue
        if Bumerarma['contador'] > Bumerarma['tempo']:

            dx = john.x - Bumerarma['sprite'].x
            dy = john.y - Bumerarma['sprite'].y
            dt = abs(dx) + abs(dy)
            Bumerarma['dx'] = dx/dt
            Bumerarma['dy'] = dy/dt

            # desativa a arma caso tenha voltado
            if -1 < dx < 1 and -1 < dy < 1:

                Bumerarma['ativo?'] = False
                Bumerarma['contador'] = 0
                Bumerarma['dano'] = 0

        #atualizações gerais
        if nivelBumer == 1:
            Bumerarma['dano'] = 0.5
        elif nivelBumer == 2:
            Bumerarma['dano'] = 0.7
        elif nivelBumer == 3:
            Bumerarma['dano'] = 1.5
        elif nivelBumer == 4:
            Bumerarma['dano'] = 1.7
        elif nivelBumer == 5:
            Bumerarma['dano'] = 2.5
        Bumerarma['sprite'].x += (velJohnX + Bumerarma['dx'] * Bumerarma['vel']) * janela.delta_time()
        Bumerarma['sprite'].y += (velJohnY + Bumerarma['dy'] * Bumerarma['vel']) * janela.delta_time()
        Bumerarma['contador'] += janela.delta_time()
        Bumerarma['sprite'].update()
        Bumerarma['sprite'].draw()

    if Summon['ativo?']:

        Summon['sprite'].x = john.x + john.width / 2 + 160 * cos(Summon['contador']) - Summon['sprite'].width / 2 + velJohnX * janela.delta_time()
        Summon['sprite'].y = john.y + john.height / 2 + 160 * sin(Summon['contador']) - Summon['sprite'].height / 2 + velJohnY * janela.delta_time()
        Summon['contador'] += 3.5 * janela.delta_time()
        Summon['dano'] = 1.5

        Summon['sprite'].update()
        Summon['sprite'].draw()


def ativaBumerangue(Mouse, Bumerarma, john):

    # define a posição do mouse
    X = Mouse.get_position()[0]
    Y = Mouse.get_position()[1]

    # atira o bumerangue na direção do mouse, caso seja ativado
    if Mouse.is_button_pressed(1) and not Bumerarma['ativo?']:
        Bumerarma['ativo?'] = True
        dx = X - john.x - john.width / 2
        dy = Y - john.y - john.height / 2
        dt = abs(dx) + abs(dy)
        Bumerarma['dx'] = dx / dt
        Bumerarma['dy'] = dy / dt


def carregaAmber(amberPode, janela, vetAmber, Mouse, john, timerAmber, mouseApertado, velAmber, danoAmber, aumentou, nivel):

    '''
    Essa função controla o comportamento do projetil da amber enquanto ele ainda não foi atirado.
    '''

    tmp = 3
    raio = 30

    if nivel >= 3:
        tmp = 5
        if timerAmber >= 5:
            raio = 50

    if nivel == 5:
        tmp = 7
        if timerAmber >= 7:
            raio = 70

    if timerAmber < tmp:
        vetAmber[-1][3] += (janela.delta_time() * nivel ** (1/2)) / 2.5
    X = Mouse.get_position()[0]
    Y = Mouse.get_position()[1]
    dx = X - john.x - john.width / 2
    dy = Y - john.y - john.height / 2
    dt = abs(dx) + abs(dy)
    vetAmber[-1][1] = dx / dt * velAmber
    vetAmber[-1][2] = dy / dt * velAmber
    angulo = atan2(dy, dx)
    if timerAmber >= 3 and not aumentou:
        vetAmber[-1][0] = Sprite("Sprites/amberProjetil-grande.png")
        vetAmber[-1][3] += 0.7
        aumentou = True
    if timerAmber >= 5 and nivel >= 3:
        vetAmber[-1][0] = Sprite("Sprites/Amber_Gigante.png")
    if timerAmber >= 7 and nivel == 5:
        vetAmber[-1][0] = Sprite("Sprites/Amber_Gigantesca.png")
    vetAmber[-1][0].set_position(janela.width / 2 - vetAmber[-1][0].width / 2 + raio * cos(angulo), janela.height / 2 - vetAmber[-1][0].height / 2 + raio * sin(angulo))
    #vetAmber[-1][0].draw()

    if not Mouse.is_button_pressed(1) and mouseApertado:
        vetAmber[-1][3] += danoAmber
        vetAmber[-1][5] = True
        timerAmber = 0
    return vetAmber[-1][5], timerAmber, aumentou


def atualizaAmber(vetAmber, velJohnX, velJohnY, janela, nivel):

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
            0].y > janela.height or vetAmber[i][4] > 50 + nivel * 8:
            vetAmber.pop(i)
            break


def atualizaBipper(vetBipper, janela, velJohnX, velJohnY):

    '''
    Essa função define o comportamento dos projeteis bipper após serem criados.
    '''

    for i in range(len(vetBipper)):
        vetBipper[i][0].x += (vetBipper[i][1] + velJohnX) * janela.delta_time()
        vetBipper[i][0].y += (vetBipper[i][2] + velJohnY) * janela.delta_time()
        vetBipper[i][0].draw()

    for i in range(len(vetBipper)):
        if vetBipper[i][0].x < 0 or vetBipper[i][0].x > janela.width or vetBipper[i][0].y < 0 or vetBipper[i][
            0].y > janela.height:
            vetBipper.pop(i)
            break


def colisãoDano(inimigo, tiroB, tiroA, danoB, Bumerarma, Summon):

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
        if Bumerarma['sprite'].collided(i[0]) and Bumerarma['ativo?']:
            i[1] -= Bumerarma['dano']
        if Summon['sprite'].collided(i[0]):
            i[1] -= Summon['dano']


        # se houver colisão com a bipper, o tiro some.
        for j in range(len(tiroB)):
            if tiroB[j][0].collided(i[0]):
                tiroB.pop(j)
                break
