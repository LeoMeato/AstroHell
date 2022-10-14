from PPlay.window import *
from PPlay.sprite import *
from PPlay.animation import *
from menu import *
from jogar import *
import random

# setup geral

janela = Window(1280, 720)
janela.set_title("AstroHell")
Mouse = janela.get_mouse()
teclado = janela.get_keyboard()

fundo = Sprite("mapa2.png")
dx = (fundo.width - janela.width) / 2
dy = (fundo.height - janela.height) / 2
fundo.set_position(-dx, -dy)

# setup menu sprites

BotaoJogar = Sprite("Jogar(1).png")
BotaoConfiguraçoes = Sprite("Config(1).png")
BotaoSair = Sprite("Sair(1).png")
Logo = Sprite("astrohell.png")

BotaoJogar.set_position(janela.width / 2 - BotaoJogar.width / 2, janela.height/2 - 40)
BotaoConfiguraçoes.set_position(janela.width / 2 - BotaoConfiguraçoes.width / 2, janela.height/2 + 80)
BotaoSair.set_position(janela.width / 2 - BotaoSair.width / 2, janela.height/2 + 200)
Logo.set_position(janela.width / 2 - Logo.width / 2, 80)

# setup mapa

mapa = Sprite("mapa2.png")
dx = (mapa.width - janela.width) / 2
dy = (mapa.height - janela.height) / 2
mapa.set_position(-dx, -dy)




# Game Loop

while True:
    fundo.draw()

    resposta = menu(BotaoJogar, BotaoConfiguraçoes, BotaoSair, Logo, Mouse, janela)
    if resposta == 1:
        jogar(teclado, Mouse, janela, mapa)
    elif resposta == 2:
        print('')
    elif resposta == 3:
        break

    janela.update()
