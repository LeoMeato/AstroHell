def mapaInfinito(mapa, janela):

    if mapa.x > 0:
        mapa.x = -mapa.width + janela.width + 320
    if mapa.x < -mapa.width + janela.width:
        mapa.x = -320
    if mapa.y > 0:
        mapa.y = -mapa.height + janela.height + 80
    if mapa.y < -mapa.height + janela.height:
        mapa.y = -80


def jogar(teclado, Mouse, janela, mapa, john):

    while True:

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

        mapaInfinito(mapa, janela)

        mapa.draw()
        if teclado.key_pressed('ESC'):
            break
        john.draw()
        janela.update()