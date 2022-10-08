from PPlay.window import *
from PPlay.sprite import *
from menu import *
from jogar import *

# setup geral

janela = Window(1280, 720)
Mouse = janela.get_mouse()
teclado = janela.get_keyboard()
fundo = Sprite("mapa-fundo.png")

# setup menu sprites

BotaoJogar = Sprite("Jogar(1).png")
BotaoConfiguraçoes = Sprite("Config(1).png")
BotaoSair = Sprite("Sair(1).png")
#logo = Sprite("tmp")

BotaoJogar.set_position(janela.width / 2 - BotaoJogar.width / 2, janela.height/2 - 40)
BotaoConfiguraçoes.set_position(janela.width / 2 - BotaoConfiguraçoes.width / 2, janela.height/2 + 80)
BotaoSair.set_position(janela.width / 2 - BotaoSair.width / 2, janela.height/2 + 200)

# setup mapa

mapa = Sprite("mapa2.png")
dx = (mapa.width - janela.width) / 2
dy = (mapa.height - janela.height) / 2
mapa.set_position(-dx, -dy)

# setup player

john = Sprite("master chief.png")  # mudar sprite
john.set_position(janela.width / 2 - john.width / 2, janela.height / 2 - john.height / 2)

# Game Loop

while True:
    fundo.draw()

    resposta = menu(BotaoJogar, BotaoConfiguraçoes, BotaoSair, Mouse, janela)
    if resposta == 1:
        jogar(teclado, Mouse, janela, mapa, john)
    elif resposta == 2:
        print('')
    elif resposta == 3:
        break

    janela.update()
