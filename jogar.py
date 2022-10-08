def jogar(teclado, Mouse, janela):
    while True:
        janela.set_background_color([0, 0, 0])
        if teclado.key_pressed('ESC'):
            break
        janela.update()