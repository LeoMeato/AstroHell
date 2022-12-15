from PPlay.window import *
from jogar import *


def Enredo(janela, teclado):

    dialogo1 = Sprite("Sprites/dialogo.jpg")
    dialogo2 = Sprite("Sprites/dialogo2.png")
    dialogo1.set_position(janela.width/2 - dialogo1.width/2, janela.height)
    dialogo2.set_position(janela.width/2 - dialogo2.width/2, janela.height/2 - dialogo2.height/2)
    tempo = 0
    while True:
        janela.set_background_color([0, 0, 0])
        tempo += janela.delta_time()
        dialogo1.y -= 50 * janela.delta_time()
        if dialogo1.y + dialogo1.height < -50:
            dialogo2.draw()
        janela.draw_text("ESC para pular", janela.width - 160, janela.height - 40, size=25, color=(255, 255, 255),
                     font_name="Candara")
        if teclado.key_pressed('ESC') or tempo > 35:
            break
        dialogo1.draw()
        janela.update()


# setup geral

janela = Window(1280, 720)
janela.set_title("AstroHell")
Mouse = janela.get_mouse()
teclado = janela.get_keyboard()

fundo = Sprite("Sprites/mapa2.png")
dx = (fundo.width - janela.width) / 2
dy = (fundo.height - janela.height) / 2
fundo.set_position(-dx, -dy)

# setup menu sprites

BotaoJogar = Sprite("Sprites/Jogar(1).png")
BotaoCreditos = Sprite("Sprites/Creditos.png")
BotaoSair = Sprite("Sprites/Sair(1).png")
Logo = Sprite("Sprites/astrohell.png")

BotaoJogar.set_position(janela.width / 2 - BotaoJogar.width / 2, janela.height/2 - 40)
BotaoCreditos.set_position(janela.width / 2 - BotaoCreditos.width / 2, janela.height/2 + 80)
BotaoSair.set_position(janela.width / 2 - BotaoSair.width / 2, janela.height/2 + 200)
Logo.set_position(janela.width / 2 - Logo.width / 2, 80)

# setup mapa

mapa = Sprite("Sprites/mapa2.png")
dx = (mapa.width - janela.width) / 2
dy = (mapa.height - janela.height) / 2
mapa.set_position(-dx, -dy)

# Diálogo inicial
som_inicial = Sound("Sons/infinity.mp3")
som_inicial.set_volume(8)
som_inicial.set_repeat(1)
som_inicial.play()
Enredo(janela, teclado)

# Música inicial

# Game Loop

while True:
    fundo.draw()
    resposta = menu(BotaoJogar, BotaoCreditos, BotaoSair, Logo, Mouse, janela)
    if resposta == 1:
        som_inicial.pause()
        jogar(teclado, Mouse, janela, mapa)
    elif resposta == 2:
        creditos(Mouse, teclado, janela)
    elif resposta == 3:
        som_inicial.stop()
        break

    janela.update()
