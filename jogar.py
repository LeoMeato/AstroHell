from random import randint
from armas_funções import *
from outras_funções import *

nivelBip = 1
nivelAmber = 0
nivelBumer = 0
nivelLaser = 0

cooldownDanoJ = 0

def mapaInfinito(mapa, janela):
    if mapa.x > 0:
        mapa.x = -mapa.width + janela.width + 200 - janela.width % 200
    if mapa.x < -mapa.width + janela.width:
        mapa.x = -(200 - janela.width % 200)
    if mapa.y > 0:
        mapa.y = -mapa.height + janela.height + 200 - janela.height % 200
    if mapa.y < -mapa.height + janela.height:
        mapa.y = -(200 - janela.height % 200)


def bip(Bip, janela, velJohnX, velJohnY, velBip, john, danoBip, armadura):

    global cooldownDanoJ

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


def zeta(Zeta, janela, velJohnX, velJohnY, velZeta, john):

    Zeta.x += velJohnX * janela.delta_time()
    Zeta.y += velJohnY * janela.delta_time()
    dx = john['John'].x - Zeta.x
    dy = john['John'].y - Zeta.y
    dt = abs(dx) + abs(dy)
    if dx ** 2 + dy ** 2 > 200 ** 2:
        Zeta.x += velZeta * (dx / dt) * janela.delta_time()
        Zeta.y += velZeta * (dy / dt) * janela.delta_time()

    Zeta.draw()


def morreuInimigo(Bip, vetPeca):
    j = 0
    a = len(Bip)
    while j < a and a > 0:
        if Bip[j][1] <= 0:
            r = randint(1, 100)
            if r < 20:
                vetPeca.append(Sprite("Sprites/peçapequena.png"))
                vetPeca[-1].set_position(Bip[j][0].x + Bip[j][0].width / 2, Bip[j][0].y + Bip[j][0].height / 2)
            Bip.pop(j)
            a -= 1
        j += 1


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


def areaSpawn(janela):
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

    return x, y


def spawnBip(vetBip, janela):

    x, y = areaSpawn(janela)

    vetBip.append([Sprite("Sprites/bip.png"), 30])
    vetBip[-1][0].set_position(x, y)


def spawnZeta(vetZeta, janela):

    x, y = areaSpawn(janela)

    vetZeta.append([Sprite("Sprites/zeta.png"), 80])
    vetZeta[-1][0].set_position(x, y)


'''def evitaColisão(spt1, spt2):

    if spt1.x + spt1.width >= spt2.x:
        spt1.x = spt2.x - spt1.width
    elif spt1.y + spt1.height >= spt2.y:
        spt1.y = spt2.y - spt1.height
    elif spt2.x + spt2.width >= spt1.x:
        spt2.x = spt1.x - spt2.width
    elif spt2.y + spt2.height >= spt1.y:
        spt2.y = spt1.y - spt2.height'''


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

    john = {'John': Sprite("Sprites/Astronauta(3).png"), 'vida': 200, 'pregos': 40}
    john['John'].set_position(janela.width / 2 - john['John'].width / 2, janela.height / 2 - john['John'].height / 2)

    # setup inimigos

    vetBip = [[Sprite("Sprites/bip.png"), 30], [Sprite("Sprites/bip.png"), 30], [Sprite("Sprites/bip.png"), 30]]
    vetBip[0][0].set_position(-100, 620)
    vetBip[1][0].set_position(700, -200)
    vetBip[2][0].set_position(2300, 500)

    vetZeta = []

    # setup obstáculos
    ## Daria pra botar todos os obstáculos em uma só lista, mas fiz assim pra poder diferenciar mais fácil, por enquanto.
    vetArvores = [Sprite("Sprites/árvore_pequena.png"), Sprite("Sprites/árvore_pequena.png"), Sprite(
        "Sprites/árvore_pequena.png")]
    vetArvores[0].set_position(200, 200)
    vetArvores[1].set_position(700, 800)
    vetArvores[2].set_position(1000, 300)

    vetPedras = [Sprite("Sprites/pedra1peq.png"), Sprite("Sprites/pedra1peq.png"), Sprite("Sprites/pedra1peq.png"), Sprite(
        "Sprites/pedra1peq.png"),
                 Sprite("Sprites/pedra1peq.png")]
    vetPedras[0].set_position(350, 250)
    vetPedras[1].set_position(250, 400)
    vetPedras[2].set_position(400, 600)
    vetPedras[3].set_position(200, 700)
    vetPedras[4].set_position(700, 500)

    vetPeca = [Sprite("Sprites/peçapequena.png")]
    ## Tentei criar em um For pra ficar aleatorio, mas tem vezes que nasce em cima da pedra/arvore
    for i in range(len(vetPeca)):
        vetPeca[i].set_position((i + 1) * randint(100, 200), (i + 1) * randint(100, 200))

    # setup geral

    global cooldownDanoJ

    global nivelBip
    global nivelBumer
    global nivelLaser
    global nivelAmber

    armadura = 1

    tempo_de_jogo = 0

    nivelBip = 1
    nivelAmber = 0
    nivelBumer = 0
    nivelLaser = 0

    armadura = 1

    gameover = False

    # setup dos bips e zetas

    velBip = 80
    danoBip = 10

    velZeta = 90

    # setup cooldowns, timers e contadores

    cooldownB = 0
    cooldownSpawnBip = 0
    cooldownSpawnZeta = 0
    cooldownDanoJ
    cooldownA = 0

    timerAmber = 0

    amberPiercing = 0

    # setup da bipper

    velTiro = 900
    danoBipper = 10
    vetBipper = []

    # setup da amber

    velAmber = 700
    danoAmber = 0.6
    vetAmber = []
    amberPode = True

    mouseApertado = False

    Arma = 1

    # setup HUD

    vida = Sprite("Sprites/9vidas.png")
    vida.x = janela.width / 2 - vida.width / 2
    vida.y = janela.height - vida.height - 25
    bipper_lateral = Sprite("Sprites/bipper_lateral.png")
    bipper_lateral.x = 10
    bipper_lateral.y = 170
    bumerangue_lateral = Sprite("Sprites/bumerangue_lateral_desabilitado.png")
    bumerangue_lateral.x = 10
    bumerangue_lateral.y = bipper_lateral.y + bumerangue_lateral.height + 15
    canhao_lateral = Sprite("Sprites/canhao_lateral_desabilitado.png")
    canhao_lateral.x = 10
    canhao_lateral.y = bumerangue_lateral.y + canhao_lateral.height + 15
    amber_lateral = Sprite("Sprites/amber_lateral_desabilitada.png")
    amber_lateral.x = 10
    amber_lateral.y = canhao_lateral.y + amber_lateral.height + 15
    pausa = Sprite("Sprites/pausa.png")
    pausa.x = 10
    pausa.y = 10
    pecas_hud = Sprite("Sprites/uma peça.png")
    pecas_hud.x = janela.width - pecas_hud.width - 30
    pecas_hud.y = 15

    # fps

    soma_fps = 0
    contador_fps = 0
    printfps = 0

    while True:

        # mudanças de mecânicas atreladas aos niveis

        if nivelBip == 2:
            danoBipper = 15
            velTiro = 1000
        if nivelBip == 3:
            danoBipper = 20

        # cooldowns e timers

        cooldownB -= (20 + (nivelBip * 2) ** 1.7) * janela.delta_time()
        cooldownSpawnBip -= 15 * janela.delta_time()
        cooldownSpawnZeta -= 1.5 * janela.delta_time()
        cooldownDanoJ -= 15 * janela.delta_time()
        cooldownA -= 20 * janela.delta_time()

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

        # escolha da arma

        if teclado.key_pressed('1'):
            Arma = 1
        elif teclado.key_pressed('2') and nivelBumer >= 1:
            Arma = 2
        elif teclado.key_pressed('3') and nivelLaser >= 1:
            Arma = 3
        elif teclado.key_pressed('4') and nivelAmber >= 1:
            Arma = 4

        if Arma == 1:
            # criação de pojeteis da bipper
            cooldownB = tiroBipper(janela, Mouse, john['John'], velTiro, vetBipper, cooldownB)
        elif Arma == 2:
            pass
        elif Arma == 3:
            pass
        elif Arma == 4:
            if cooldownA <= 0:
                amberPode, cooldownA = tiroAmber(janela, vetAmber, Mouse, john['John'], velAmber, amberPode, cooldownA)
            if not amberPode:
                timerAmber += janela.delta_time()
                amberPode, timerAmber = carregaAmber(amberPode, janela, vetAmber, Mouse, john['John'], timerAmber,
                                                     mouseApertado, velAmber, danoAmber)
            else:
                timerAmber = 0

        # colisão com dano

        colisãoDano(vetBip, vetBipper, vetAmber, danoBipper)

        # comportamento dos bips

        if cooldownSpawnBip <= 0:
            spawnBip(vetBip, janela)
            cooldownSpawnBip = 25

        for i in range(len(vetBip)):
            bip(vetBip[i][0], janela, velJohnX, velJohnY, velBip, john, danoBip, armadura)

        # comportamento dos zetas

        if cooldownSpawnZeta <= 0:
            if tempo_de_jogo > 0:
                spawnZeta(vetZeta, janela)
            cooldownSpawnZeta = 25

        for i in range(len(vetZeta)):
            zeta(vetZeta[i][0], janela, velJohnX, velJohnY, velZeta, john)

        # verifica se algum bip está com vida < 0 e mata o que estiver

        morreuInimigo(vetBip, vetPeca)

        # renderizar tiros

        renderizarBipper(vetBipper, janela, velJohnX, velJohnY)
        renderizaAmber(vetAmber, velJohnX, velJohnY, janela)

        # HUD

        HUD(janela, john, pecas_hud, bipper_lateral, amber_lateral, bumerangue_lateral, canhao_lateral, vida, pausa,
            nivelBip, nivelAmber, nivelLaser, nivelBumer)

        tempo_de_jogo = tempo(janela, tempo_de_jogo)

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

        # fps

        contador_fps += 1
        soma_fps += janela.delta_time()
        janela.draw_text('FPS: {}'.format(int(printfps)), janela.width - 100, janela.height - 30, 17,
                             (255, 255, 255))

        if contador_fps == 80:
            printfps = contador_fps / soma_fps
            contador_fps = 0
            soma_fps = 0

        # atualizações

        john['John'].draw()
        janela.update()

        # gameover

        if gameover:
            while True:
                janela.set_background_color([0, 0, 0])
                janela.draw_text('GAME OVER', janela.width / 2 - 200, janela.height / 2 - 60, 80, (255, 255, 255), "Candara")
                janela.draw_text('Aperte ESC para voltar ao menu principal', janela.width - 550, janela.height - 30, 30, (255, 255, 255), "Candara")
                if teclado.key_pressed('ESC'):
                    break
                janela.update()
            break
