from PPlay.window import *
from PPlay.sprite import *
from menu import *

janela = Window(1280, 720)

fundo = Sprite("mapa-fundo.png")

while True:
    fundo.draw()
    janela.update()
    #resposta = menu()
