from PPlay.window import *
from PPlay.sprite import *
from menu import *

janela = Window(1280, 720)

Mouse = janela.get_mouse()

teclado = janela.get_keyboard()

fundo = Sprite("mapa-fundo.png")

while True:
    fundo.draw()
    janela.update()
    #resposta = menu(BotaoJogar, BotaoConfiguraçoes, BotaoSair, Mouse, janela, logo)
    #if resposta == 1:
    #    jogar(teclado, Mouse, janela)
