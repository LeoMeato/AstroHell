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

# Game Loop

while True:
    fundo.draw()

    resposta = menu(BotaoJogar, BotaoConfiguraçoes, BotaoSair, Mouse, janela)
    if resposta == 1:
        jogar(teclado, Mouse, janela)
    elif resposta == 2:
        print('')
    elif resposta == 3:
        break

    janela.update()
