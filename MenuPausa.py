from PPlay.window import *
from PPlay.sprite import *

def menupausa(tempo, janela):
    mouse = janela.get_mouse()
    teclado = janela.get_keyboard()
    retomar = Sprite("Sprites/retomar.png")
    retomar.x = janela.width/2 - retomar.width/2
    retomar.y = janela.height/2 - retomar.height/2
    menupr = Sprite("Sprites/botaomenuprin2.png")
    menupr.x = retomar.x + 60
    menupr.y = 160 + retomar.y
    mapa = Sprite("Sprites/mapa2.png")
    sair = Sprite("Sprites/sair_menu.png")
    sair.x = menupr.x + 30
    sair.y = menupr.y + menupr.height + 25
    astrohell = Sprite("Sprites/astrohell_menu.png")
    astrohell.x = 30
    astrohell.y = 30
    tempo_min = int(tempo/60)
    tempo_seg = tempo - (tempo_min*60)
    while True:
        mapa.draw()
        sair.draw()
        astrohell.draw()
        menupr.draw()
        retomar.draw()
        janela.draw_text("Tempo Decorrido", janela.width/2 - 150, 50 , 42, (255, 255, 255), "Candara")
        janela.draw_text(str(int(tempo_min)) + ":" + str(format(int(tempo_seg), '02d')), janela.width/2 - 42, 92 , 42, (255, 255, 255), "Candara")
        if mouse.is_over_area((retomar.x, retomar.y), (retomar.x+retomar.width, retomar.y+retomar.height)) and mouse.is_button_pressed(1):
            break
        if mouse.is_over_area((menupr.x,menupr.y), (menupr.x + menupr.width, menupr.y + menupr.height)) and mouse.is_button_pressed(1):
            return 1
        if mouse.is_over_area((sair.x, sair.y), (sair.x + sair.width, sair.y + sair.height)) and mouse.is_button_pressed(1):
            return 2
        janela.update()