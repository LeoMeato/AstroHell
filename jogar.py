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


def bip(Bip, janela, mapa, velJohnX, velJohnY,velBip, john):
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
        dx = X - john.x
        dy = Y - john.y
        dt = abs(dx) + abs(dy)
        vetBipper[0].append(Sprite("projetil_bipper.png"))
        vetBipper[0][-1].set_position(janela.width / 2, janela.height / 2)
        vetBipper[1][0].append(dx/dt * velTiro)
        vetBipper[1][1].append(dy/dt * velTiro)
        cooldownB += 10
    return cooldownB

def renderizarBipper(vetBipper, janela, velJohnX, velJohnY):
    for i in range(len(vetBipper[0])):
        vetBipper[0][i].x += (vetBipper[1][0][i] + velJohnX) * janela.delta_time()
        vetBipper[0][i].y += (vetBipper[1][1][i] + velJohnY) * janela.delta_time()
        vetBipper[0][i].draw()

    i = 0
    a = len(vetBipper[0])
    while i < a and a > 0:
        if vetBipper[0][i].x < 0 or vetBipper[0][i].x > janela.width or vetBipper[0][i].y < 0 or vetBipper[0][i].y > janela.height:
            vetBipper[0].pop(i)
            vetBipper[1][0].pop(i)
            vetBipper[1][1].pop(i)
            a -= 1
        i += 1


def jogar(teclado, Mouse, janela, mapa, john, vetBip, vetArvores, vetPedras, vetPeca):

    projetil_bipper = Sprite("projetil_bipper.png")
    vel_bipper = 400
    saiu_agora = False
    na_tela = False
    velBip = 100
    timer = 0

    cooldownB = 0

    velTiro = 900

    vetBipper = [[], [[], []]]  # primeiro para tiros e segundo para velocidade de cada tiro, que por sua vez tem o x e y

    while True:

        cooldownB -= 35 * janela.delta_time()

        velJohnX = 0
        velJohnY = 0

        if teclado.key_pressed('W'):
            velJohnY = 500
        if teclado.key_pressed('A'):
            velJohnX = 500
        if teclado.key_pressed('S'):
            velJohnY = -500
        if teclado.key_pressed('D'):
            velJohnX = -500

        mapa.x += velJohnX * janela.delta_time()
        mapa.y += velJohnY * janela.delta_time()

        mapaInfinito(mapa, janela)  # Leonardo

        mapa.draw()

        if not na_tela:
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
         #               vetTiro.pop(i)

        cooldownB = tiroComMouseBipper(janela, Mouse, projetil_bipper, john, velTiro, vetBipper, cooldownB)
        renderizarBipper(vetBipper, janela, velJohnX, velJohnY)


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

        # comportamento dos bips

        for i in range(len(vetBip)):
            bip(vetBip[i], janela, mapa, velJohnX, velJohnY, velBip, john)

        if teclado.key_pressed('ESC'):
            break

        john.draw()
        janela.update()