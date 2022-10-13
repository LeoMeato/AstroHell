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

# setup player

john = Sprite("Astronauta(3).png")
john.set_position(janela.width / 2 - john.width / 2, janela.height / 2 - john.height / 2)

# setup inimigos

vetBip = [[Sprite("bip.png"), 30], [Sprite("bip.png"), 30], [Sprite("bip.png"), 30]]
vetBip[0][0].set_position(300, 620)
vetBip[1][0].set_position(700, 200)
vetBip[2][0].set_position(600, 500)

# setup obstáculos
## Daria pra botar todos os obstáculos em uma só lista, mas fiz assim pra poder diferenciar mais fácil, por enquanto.
vetArvores = [Sprite("árvore_pequena.png"), Sprite("árvore_pequena.png"), Sprite("árvore_pequena.png")]
vetArvores[0].set_position(200,200)
vetArvores[1].set_position(700,800)
vetArvores[2].set_position(1000,300)

vetPedras = [Sprite("pedra1peq.png"), Sprite("pedra1peq.png"), Sprite("pedra1peq.png"), Sprite("pedra1peq.png"), Sprite("pedra1peq.png")]
vetPedras[0].set_position(350,250)
vetPedras[1].set_position(250,400)
vetPedras[2].set_position(400,600)
vetPedras[3].set_position(200,700)
vetPedras[4].set_position(700,500)

vetPeca = [Sprite("peçapequena.png"), Sprite("peçapequena.png"), Sprite("peçapequena.png"), Sprite("peçapequena.png"), Sprite("peçapequena.png")]
## Tentei criar em um For pra ficar aleatorio, mas tem vezes que nasce em cima da pedra/arvore
for i in range(len(vetPeca)):
    vetPeca[i].set_position((i+1)*random.randint(100, 200), (i+1)*random.randint(100, 200))


# Game Loop

while True:
    fundo.draw()

    resposta = menu(BotaoJogar, BotaoConfiguraçoes, BotaoSair, Logo, Mouse, janela)
    if resposta == 1:
        jogar(teclado, Mouse, janela, mapa, john, vetBip, vetArvores, vetPedras, vetPeca)
    elif resposta == 2:
        print('')
    elif resposta == 3:
        break

    janela.update()
