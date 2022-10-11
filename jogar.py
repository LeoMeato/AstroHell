from PPlay.window import *
from PPlay.sprite import *
from PPlay.animation import *


def mapaInfinito(mapa, janela):
    if mapa.x > 0:
        mapa.x = -mapa.width + janela.width + 200 - janela.width % 200
    if mapa.x < -mapa.width + janela.width:
        mapa.x = -(200 - janela.width % 200)
    if mapa.y > 0:
        mapa.y = -mapa.height + janela.height + 200 - janela.height % 200
    if mapa.y < -mapa.height + janela.height:
        mapa.y = -(200 - janela.height % 200)


def bip(Bip, janela, mapa, velJohnX, velJohnY, velBip, john):
    Bip.x += velJohnX * janela.delta_time()
    Bip.y += velJohnY * janela.delta_time()
    dx = john.x - Bip.x
    dy = john.y - Bip.y
    dt = abs(dx) + abs(dy)
    Bip.x += velBip * (dx / dt) * janela.delta_time()
    Bip.y += velBip * (dy / dt) * janela.delta_time()
    Bip.draw()


def tiroComMouseBipper(janela, Mouse, projetil_bipper, john, velTiro, vetBipper, cooldownB):
    X = Mouse.get_position()[0]
    Y = Mouse.get_position()[1]
    if Mouse.is_button_pressed(1) and cooldownB <= 0:
        vetBipper.append([])
        dx = X - john.x
        dy = Y - john.y
        dt = abs(dx) + abs(dy)
        vetBipper[-1].append(Sprite("projetil_bipper.png"))
        vetBipper[-1][0].set_position(janela.width / 2, janela.height / 2)
        vetBipper[-1].append(dx / dt * velTiro)
        vetBipper[-1].append(dy / dt * velTiro)
        cooldownB = 10
    return cooldownB


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


def colisãoDano(inimigo, tiro, dano):
    for i in inimigo:
        for j in tiro:
            if i[0].collided(j[0]):
                i[1] -= dano
        j = 0
        a = len(tiro)
        while j < a and a > 0:
            if tiro[j][0].collided(i[0]):
                tiro.pop(j)
                a -= 1
            j += 1


def morreuInimigo(Bip):
    j = 0
    a = len(Bip)
    while j < a and a > 0:
        if Bip[j][1] <= 0:
            Bip.pop(j)
            a -= 1
        j += 1


def jogar(teclado, Mouse, janela, mapa, john, vetBip, vetArvores, vetPedras, vetPeca):
    projetil_bipper = Sprite("projetil_bipper.png")
    vel_bipper = 400
    saiu_agora = False
    na_tela = False
    velBip = 100
    timer = 0

    danoBipper = 10

    cooldownB = 0

    velTiro = 900

    vetBipper = []

    while True:

        cooldownB -= 20 * janela.delta_time()

        velJohnX = 0
        velJohnY = 0

        if teclado.key_pressed('W'):
            velJohnY = 400
        if teclado.key_pressed('A'):
            velJohnX = 400
        if teclado.key_pressed('S'):
            velJohnY = -400
        if teclado.key_pressed('D'):
            velJohnX = -400

        mapa.x += velJohnX * janela.delta_time()
        mapa.y += velJohnY * janela.delta_time()

        mapaInfinito(mapa, janela)

        mapa.draw()

        '''if not na_tela:
            if teclado.key_pressed("SPACE"):
                na_tela = True
                saiu_agora = True
        if saiu_agora:
            projetil_bipper.x = john.x + john.width / 2
            projetil_bipper.y = john.y - 15
            saiu_agora = False
        if na_tela:
            projetil_bipper.y -= (vel_bipper * janela.delta_time())
            projetil_bipper.draw()
            if projetil_bipper.y <= 0:
                projetil_bipper.y = janela.height
                na_tela = False

        #        for n in range(1, len(vetTiro)):
     #           if len(vetTiro) >= n:
      #              if vetTiro[i].x >= 0 or vetTiro[i] <= 0:
       #                 vetTiro.pop(i)
        #            if vetTiro[i].x >= janela.width or vetTiro[i].y >= janela.height:
         #               vetTiro.pop(i)'''  # pode apagar?

        for i in range(len(vetArvores)):
            vetArvores[i].draw()
            vetArvores[i].x += velJohnX * janela.delta_time()
            vetArvores[i].y += velJohnY * janela.delta_time()

        for n in range(5):
            vetPedras[n].draw()
            vetPedras[n].x += velJohnX * janela.delta_time()
            vetPedras[n].y += velJohnY * janela.delta_time()

        for i in range(len(vetPeca)):
            vetPeca[i].draw()
            vetPeca[i].x += velJohnX * janela.delta_time()
            vetPeca[i].y += velJohnY * janela.delta_time()

        # comportamento da bipper

        cooldownB = tiroComMouseBipper(janela, Mouse, projetil_bipper, john, velTiro, vetBipper, cooldownB)
        renderizarBipper(vetBipper, janela, velJohnX, velJohnY)

        # colisão com dano

        colisãoDano(vetBip, vetBipper, danoBipper)

        # comportamento dos bips

        for i in range(len(vetBip)):
            bip(vetBip[i][0], janela, mapa, velJohnX, velJohnY, velBip, john)

        # verifica se algum bip está com vida < 0 e mata o que estiver

        morreuInimigo(vetBip)

        if teclado.key_pressed('ESC'):
            break

        john.draw()
        janela.update()
