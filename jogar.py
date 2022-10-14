from PPlay.window import *
from PPlay.sprite import *
from PPlay.animation import *
from random import randint

tempo_de_jogo = 0

nivelBip = 1
nivelAmber = 0
nivelBumer = 0
nivelLaser = 0

cooldownDanoJ = 0

armadura = 1

def mapaInfinito(mapa, janela):
    if mapa.x > 0:
        mapa.x = -mapa.width + janela.width + 200 - janela.width % 200
    if mapa.x < -mapa.width + janela.width:
        mapa.x = -(200 - janela.width % 200)
    if mapa.y > 0:
        mapa.y = -mapa.height + janela.height + 200 - janela.height % 200
    if mapa.y < -mapa.height + janela.height:
        mapa.y = -(200 - janela.height % 200)


def bip(Bip, janela, mapa, velJohnX, velJohnY, velBip, john, danoBip):

    global cooldownDanoJ
    global armadura

    Bip.x += velJohnX * janela.delta_time()
    Bip.y += velJohnY * janela.delta_time()
    dx = john['John'].x - Bip.x
    dy = john['John'].y - Bip.y
    dt = abs(dx) + abs(dy)
    Bip.x += velBip * (dx / dt) * janela.delta_time()
    Bip.y += velBip * (dy / dt) * janela.delta_time()
    if Bip.collided(john['John']) and cooldownDanoJ <= 0:
        john['vida'] -= danoBip * armadura
        cooldownDanoJ = 20
    Bip.draw()


def tiroComMouseBipper(janela, Mouse, john, velTiro, vetBipper, cooldownB):
    X = Mouse.get_position()[0]
    Y = Mouse.get_position()[1]
    if Mouse.is_button_pressed(1) and cooldownB <= 0:
        vetBipper.append([])
        dx = X - john.x - john.width / 2
        dy = Y - john.y - john.height / 2
        dt = abs(dx) + abs(dy)
        vetBipper[-1].append(Sprite("projetil_bipper.png"))
        vetBipper[-1][0].set_position(janela.width / 2, janela.height / 2)
        vetBipper[-1].append(dx / dt * velTiro)
        vetBipper[-1].append(dy / dt * velTiro)
        cooldownB = 10
    return cooldownB


def renderizarBipper(vetBipper, janela, velJohnX, velJohnY):
    for i in range(len(vetBipper)):
        vetBipper[i][0].x += (vetBipper[i][1] + velJohnX) * janela.delta_time()
        vetBipper[i][0].y += (vetBipper[i][2] + velJohnY) * janela.delta_time()
        vetBipper[i][0].draw()

    i = 0
    a = len(vetBipper)
    while i < a and a > 0:
        if vetBipper[i][0].x < 0 or vetBipper[i][0].x > janela.width or vetBipper[i][0].y < 0 or vetBipper[i][
            0].y > janela.height:
            vetBipper.pop(i)
            a -= 1
        i += 1


def colisãoDano(inimigo, tiro, dano):
    for i in inimigo:
        for j in tiro:
            if i[0].collided(j[0]):
                i[1] -= dano
        j = 0
        a = len(tiro)
        while j < a and a > 0:
            if tiro[j][0].collided(i[0]):
                tiro.pop(j)
                a -= 1
            j += 1


def morreuInimigo(Bip, vetPeca):
    j = 0
    a = len(Bip)
    while j < a and a > 0:
        if Bip[j][1] <= 0:
            r = randint(1, 100)
            if r < 20:
                vetPeca.append(Sprite("peçapequena.png"))
                vetPeca[-1].set_position(Bip[j][0].x + Bip[j][0].width / 2, Bip[j][0].y + Bip[j][0].height / 2)
            Bip.pop(j)
            a -= 1
        j += 1


def tempo(janela):
    global tempo_de_jogo
    tempo_de_jogo += janela.delta_time()
    tempo_de_jogo_min = tempo_de_jogo // 60
    tempo_de_jogo_seg = tempo_de_jogo - tempo_de_jogo_min * 60
    janela.draw_text("{}:{:0>2}".format(int(tempo_de_jogo_min), int(tempo_de_jogo_seg)), janela.width / 2 - 20, 17, 40,
                     (255, 255, 255), "Candara")

def peças(vetPeca, john, velJohnX, velJohnY, janela):
    for i in range(len(vetPeca)):
        vetPeca[i].draw()
        vetPeca[i].x += velJohnX * janela.delta_time()
        vetPeca[i].y += velJohnY * janela.delta_time()
        if vetPeca[i].collided(john['John']):
            john['pregos'] += 1
    j = 0
    a = len(vetPeca)
    while j < a and a > 0:
        if vetPeca[j].collided(john['John']):
            vetPeca.pop(j)
            a -= 1
        j += 1

def spawnBip(vetBip, janela):
    r = randint(1, 4)

    x = 0
    y = 0

    if r == 1:
        x = randint(janela.width, janela.width * 1.5)
        y = randint(-300, janela.height + 300)
    elif r == 2:
        x = randint(-janela.width * 1.5, 0)
        y = randint(-300, janela.height + 300)
    elif r == 3:
        x = randint(0, janela.width)
        y = randint(-janela.height, 0)
    elif r == 4:
        x = randint(0, janela.width)
        y = randint(janela.height, janela.height * 1.5)

    vetBip.append([Sprite("bip.png"), 30])
    vetBip[-1][0].set_position(x, y)

def niveisDeArma(mouseApertado, john, Mouse, janela, bipper_lateral, bumerangue_lateral, amber_lateral, canhao_lateral):

    global nivelBip
    global nivelBumer
    global nivelLaser
    global nivelAmber

    if not mouseApertado and Mouse.is_button_pressed(1) and bipper_lateral.x + bipper_lateral.width - 20\
            < Mouse.get_position()[0] < bipper_lateral.x + bipper_lateral.width and bipper_lateral.y\
            + bipper_lateral.height - 20 < Mouse.get_position()[1] < bipper_lateral.y + bipper_lateral.height:
        if nivelBip == 1 and john['pregos'] >= 10:
            john['pregos'] -= 10
            nivelBip = 2
        elif nivelBip == 2 and john['pregos'] >= 15:
            john['pregos'] -= 15
            nivelBip = 3
        elif nivelBip == 3 and john['pregos'] >= 20:
            john['pregos'] -= 20
            nivelBip = 4
        elif nivelBip == 4 and john['pregos'] >= 30:
            john['pregos'] -= 30
            nivelBip = 5

    if not mouseApertado and Mouse.is_button_pressed(1) and amber_lateral.x + amber_lateral.width - 20\
            < Mouse.get_position()[0] < amber_lateral.x + amber_lateral.width and amber_lateral.y\
            + amber_lateral.height - 20 < Mouse.get_position()[1] < amber_lateral.y + amber_lateral.height:
        if nivelAmber == 0 and john['pregos'] >= 10:
            john['pregos'] -= 10
            nivelAmber = 1
        elif nivelAmber == 1 and john['pregos'] >= 15:
            john['pregos'] -= 15
            nivelAmber = 2
        elif nivelAmber == 2 and john['pregos'] >= 25:
            john['pregos'] -= 25
            nivelAmber = 3
        elif nivelAmber == 3 and john['pregos'] >= 35:
            john['pregos'] -= 35
            nivelAmber = 4
        elif nivelAmber == 4 and john['pregos'] >= 45:
            john['pregos'] -= 45
            nivelAmber = 5

    if not mouseApertado and Mouse.is_button_pressed(1) and bumerangue_lateral.x + bumerangue_lateral.width - 20\
            < Mouse.get_position()[0] < bumerangue_lateral.x + bumerangue_lateral.width and bumerangue_lateral.y\
            + bumerangue_lateral.height - 20 < Mouse.get_position()[1] < bumerangue_lateral.y + bumerangue_lateral.height:
        if nivelBumer == 0 and john['pregos'] >= 10:
            john['pregos'] -= 10
            nivelBumer = 1
        elif nivelBumer == 1 and john['pregos'] >= 15:
            john['pregos'] -= 15
            nivelBumer = 2
        elif nivelBumer == 2 and john['pregos'] >= 25:
            john['pregos'] -= 25
            nivelBumer = 3
        elif nivelBumer == 3 and john['pregos'] >= 35:
            john['pregos'] -= 35
            nivelBumer = 4
        elif nivelBumer == 4 and john['pregos'] >= 45:
            john['pregos'] -= 45
            nivelBumer = 5

    if not mouseApertado and Mouse.is_button_pressed(1) and canhao_lateral.x + canhao_lateral.width - 20\
            < Mouse.get_position()[0] < canhao_lateral.x + canhao_lateral.width and canhao_lateral.y\
            + canhao_lateral.height - 20 < Mouse.get_position()[1] < canhao_lateral.y + canhao_lateral.height:
        if nivelLaser == 0 and john['pregos'] >= 10:
            john['pregos'] -= 10
            nivelLaser = 1
        elif nivelLaser == 1 and john['pregos'] >= 15:
            john['pregos'] -= 15
            nivelLaser = 2
        elif nivelLaser == 2 and john['pregos'] >= 25:
            john['pregos'] -= 25
            nivelLaser = 3
        elif nivelLaser == 3 and john['pregos'] >= 35:
            john['pregos'] -= 35
            nivelLaser = 4
        elif nivelLaser == 4 and john['pregos'] >= 45:
            john['pregos'] -= 45
            nivelLaser = 5


def jogar(teclado, Mouse, janela, mapa):

    # setup player

    john = {'John': Sprite("Astronauta(3).png"), 'vida': 200, 'pregos': 300}
    john['John'].set_position(janela.width / 2 - john['John'].width / 2, janela.height / 2 - john['John'].height / 2)

    # setup inimigos

    vetBip = [[Sprite("bip.png"), 30], [Sprite("bip.png"), 30], [Sprite("bip.png"), 30]]
    vetBip[0][0].set_position(-100, 620)
    vetBip[1][0].set_position(700, -200)
    vetBip[2][0].set_position(2300, 500)

    # setup obstáculos
    ## Daria pra botar todos os obstáculos em uma só lista, mas fiz assim pra poder diferenciar mais fácil, por enquanto.
    vetArvores = [Sprite("árvore_pequena.png"), Sprite("árvore_pequena.png"), Sprite("árvore_pequena.png")]
    vetArvores[0].set_position(200, 200)
    vetArvores[1].set_position(700, 800)
    vetArvores[2].set_position(1000, 300)

    vetPedras = [Sprite("pedra1peq.png"), Sprite("pedra1peq.png"), Sprite("pedra1peq.png"), Sprite("pedra1peq.png"),
                 Sprite("pedra1peq.png")]
    vetPedras[0].set_position(350, 250)
    vetPedras[1].set_position(250, 400)
    vetPedras[2].set_position(400, 600)
    vetPedras[3].set_position(200, 700)
    vetPedras[4].set_position(700, 500)

    vetPeca = [Sprite("peçapequena.png")]
    ## Tentei criar em um For pra ficar aleatorio, mas tem vezes que nasce em cima da pedra/arvore
    for i in range(len(vetPeca)):
        vetPeca[i].set_position((i + 1) * randint(100, 200), (i + 1) * randint(100, 200))

    # setup geral

    global cooldownDanoJ

    gameover = False

    # setup dos bips

    velBip = 80
    danoBip = 10

    cooldownB = 0
    cooldownSpawnBip = 0

    # setup da bipper

    velTiro = 900
    danoBipper = 10
    vetBipper = []

    mouseApertado = False

    Arma = 1

    # setup HUD

    vida = Sprite("9vidas.png")
    vida.x = janela.width / 2 - vida.width / 2
    vida.y = janela.height - vida.height - 25
    bipper_lateral = Sprite("bipper_lateral.png")
    bipper_lateral.x = 10
    bipper_lateral.y = 170
    bumerangue_lateral = Sprite("bumerangue_lateral_desabilitado.png")
    bumerangue_lateral.x = 10
    bumerangue_lateral.y = bipper_lateral.y + bumerangue_lateral.height + 15
    canhao_lateral = Sprite("canhao_lateral_desabilitado.png")
    canhao_lateral.x = 10
    canhao_lateral.y = bumerangue_lateral.y + canhao_lateral.height + 15
    amber_lateral = Sprite("amber_lateral_desabilitada.png")
    amber_lateral.x = 10
    amber_lateral.y = canhao_lateral.y + amber_lateral.height + 15
    pausa = Sprite("pausa.png")
    pausa.x = 10
    pausa.y = 10
    pecas_hud = Sprite("uma peça.png")
    pecas_hud.x = janela.width - pecas_hud.width - 30
    pecas_hud.y = 15

    while True:

        # mudanças de mecânicas atreladas aos niveis

        if nivelBip == 2:
            danoBipper = 15
            velTiro = 1000
        if nivelBip == 3:
            danoBipper = 20

        # cooldowns

        cooldownB -= (20 + (nivelBip * 2) ** 1.7) * janela.delta_time()
        cooldownSpawnBip -= 15 * janela.delta_time()
        cooldownDanoJ -= 100 * janela.delta_time()

        # velocidade de movimento do personagem

        velJohnX = 0
        velJohnY = 0

        if teclado.key_pressed('W'):
            velJohnY = 400
        if teclado.key_pressed('A'):
            velJohnX = 400
        if teclado.key_pressed('S'):
            velJohnY = -400
        if teclado.key_pressed('D'):
            velJohnX = -400

        # mapa

        mapa.x += velJohnX * janela.delta_time()
        mapa.y += velJohnY * janela.delta_time()

        mapaInfinito(mapa, janela)  # Leonardo

        mapa.draw()

        # cenario

        for i in range(len(vetArvores)):
            vetArvores[i].draw()
            vetArvores[i].x += velJohnX * janela.delta_time()
            vetArvores[i].y += velJohnY * janela.delta_time()

        for n in range(5):
            vetPedras[n].draw()
            vetPedras[n].x += velJohnX * janela.delta_time()
            vetPedras[n].y += velJohnY * janela.delta_time()

        peças(vetPeca, john, velJohnX, velJohnY, janela)

        # comportamento da bipper

        if Arma == 1:
            cooldownB = tiroComMouseBipper(janela, Mouse, john['John'], velTiro, vetBipper, cooldownB)

        renderizarBipper(vetBipper, janela, velJohnX, velJohnY)

        # colisão com dano

        colisãoDano(vetBip, vetBipper, danoBipper)

        # comportamento dos bips

        if cooldownSpawnBip <= 0:
            spawnBip(vetBip, janela)
            cooldownSpawnBip = 25

        for i in range(len(vetBip)):
            bip(vetBip[i][0], janela, mapa, velJohnX, velJohnY, velBip, john, danoBip)

        # verifica se algum bip está com vida < 0 e mata o que estiver

        morreuInimigo(vetBip, vetPeca)

        # HUD

        janela.draw_text("" + str(john['pregos']), pecas_hud.x - pecas_hud.width, 17, 40, (255, 255, 255), "Candara")

        janela.draw_text('{}'.format(nivelBip), bipper_lateral.x + bipper_lateral.width + 25,
                         bipper_lateral.y + bipper_lateral.height / 2, size=40, color=(255, 255, 255),
                         font_name="Candara")
        janela.draw_text('{}'.format(nivelAmber), amber_lateral.x + amber_lateral.width + 25,
                         amber_lateral.y + amber_lateral.height / 2, size=40, color=(255, 255, 255),
                         font_name="Candara")
        janela.draw_text('{}'.format(nivelBumer), bumerangue_lateral.x + bumerangue_lateral.width + 25,
                         bumerangue_lateral.y + bumerangue_lateral.height / 2, size=40, color=(255, 255, 255),
                         font_name="Candara")
        janela.draw_text('{}'.format(nivelLaser), canhao_lateral.x + canhao_lateral.width + 25,
                         canhao_lateral.y + canhao_lateral.height / 2, size=40, color=(255, 255, 255),
                         font_name="Candara")

        janela.draw_text('HP: {}'.format(john['vida']), vida.x + vida.width / 2 - 40, vida.y - 30, 30, (255, 255, 255), "Candara")

        tempo(janela)

        pausa.draw()
        pecas_hud.draw()
        amber_lateral.draw()
        canhao_lateral.draw()
        vida.draw()
        bumerangue_lateral.draw()
        bipper_lateral.draw()

        # niveis

        niveisDeArma(mouseApertado, john, Mouse, janela, bipper_lateral, bumerangue_lateral, amber_lateral, canhao_lateral)

        # sair

        if teclado.key_pressed('ESC'):
            break

        # auxilia pro mouse so clicar se estiver "desligado"

        if Mouse.is_button_pressed(1):
            mouseApertado = True
        else:
            mouseApertado = False

        if john['vida'] <= 0:
            gameover = True

        # atualizações

        john['John'].draw()
        janela.update()

        # gameover

        if gameover:
            while True:
                janela.set_background_color([0, 0, 0])
                janela.draw_text('Aperte ESC para voltar ao menu principal', janela.width - 550, janela.height - 30, 30, (255, 255, 255), "Candara")
                if teclado.key_pressed('ESC'):
                    break
                janela.update()
            break
