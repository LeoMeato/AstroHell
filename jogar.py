def mapaInfinito(mapa, janela):

    if mapa.x > 0:
        mapa.x = -mapa.width + janela.width + 320
    if mapa.x < -mapa.width + janela.width:
        mapa.x = -320
    if mapa.y > 0:
        mapa.y = -mapa.height + janela.height + 80
    if mapa.y < -mapa.height + janela.height:
        mapa.y = -80


def bip(Bip, janela, mapa, velJohnX, velJohnY,velBip, john):
    Bip.x += velJohnX * janela.delta_time()
    Bip.y += velJohnY * janela.delta_time()
    dx = john.x - Bip.x
    dy = john.y - Bip.y
    dt = abs(dx) + abs(dy)
    Bip.x += velBip * (dx / dt) * janela.delta_time()
    Bip.y += velBip * (dy / dt) * janela.delta_time()
    Bip.draw()


def jogar(teclado, Mouse, janela, mapa, john, vetBip):

    velBip = 100

    while True:

        velJohnX = 0
        velJohnY = 0

        if teclado.key_pressed('W'):
            velJohnY = 300
        if teclado.key_pressed('A'):
            velJohnX = 300
        if teclado.key_pressed('S'):
            velJohnY = -300
        if teclado.key_pressed('D'):
            velJohnX = -300

        mapa.x += velJohnX * janela.delta_time()
        mapa.y += velJohnY * janela.delta_time()

        mapaInfinito(mapa, janela)  # Leonardo

        mapa.draw()

        # comportamento dos bips

        for i in range(len(vetBip)):
            bip(vetBip[i], janela, mapa, velJohnX, velJohnY, velBip, john)

        if teclado.key_pressed('ESC'):
            break

        john.draw()
        janela.update()