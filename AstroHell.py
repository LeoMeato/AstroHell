from PPlay.window import *
from PPlay.sprite import *
from menu import *

janela = Window(1280, 720)

Mouse = janela.get_mouse()

fundo = Sprite("mapa-fundo.png")

while True:
    fundo.draw()
    janela.update()
    #resposta = menu(BotaoJogar, BotaoConfiguraçoes, BotaoSair, Mouse, janela, logo)
