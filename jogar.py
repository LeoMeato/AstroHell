from armas_funções import *
from outras_funções import *
from PPlay.animation import *
from menu import *
from inimigos_funções import *
from math import ceil

nivelBip = 1
nivelAmber = 0
nivelBumer = 0
nivelLaser = 0

cooldownDanoJ = 0

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

    john = {'John': Sprite("Sprites/Astronauta(3).png"), 'vida': 90, 'pregos': 500, 'correndo?': False, 'direcao': 1}
    john['John'].set_position(janela.width / 2 - john['John'].width / 2, janela.height / 2 - john['John'].height / 2)

    johnParado = Sprite("Sprites/Astronauta(3).png")
    johnParado.set_position(janela.width / 2 - john['John'].width / 2, janela.height / 2 - john['John'].height / 2)

    johnParadoInv = Sprite("Sprites/Astronauta(3)_invertido.png")
    johnParadoInv.set_position(janela.width / 2 - john['John'].width / 2, janela.height / 2 - john['John'].height / 2)

    johnCorrendo = Animation("Sprites/Astronauta(4).png", 4)
    johnCorrendo.set_sequence_time(0, 3, 100)
    johnCorrendo.set_position(janela.width / 2 - john['John'].width / 2, janela.height / 2 - john['John'].height / 2)

    johnCorrendoInv = Animation("Sprites/Astronauta(4)_invertido.png", 4)
    johnCorrendoInv.set_sequence_time(0, 3, 100)
    johnCorrendoInv.set_position(janela.width / 2 - john['John'].width / 2, janela.height / 2 - john['John'].height / 2)

    posRelativa = [john['John'].x, john['John'].y]

    # setup inimigos

    vetBip = [[Sprite("Sprites/bip.png"), 30], [Sprite("Sprites/bip.png"), 30], [Sprite("Sprites/bip.png"), 30]]
    vetBip[0][0].set_position(-100, 620)
    vetBip[1][0].set_position(700, -200)
    vetBip[2][0].set_position(2300, 500)

    vetZeta = []

    vetKaze = []

    boss = {'spriteAtual': 0, 'vida': 1200, 'dano': 35, 'dash': False, 'velDash': 2000, 'alvo': 0, 'cooldown': 0, 'parado': Animation("Sprites/boss_parado.png", 9), 'correndo': Animation("Sprites/correndoVetor.png", 6), 'atacando': Animation("Sprites/NightBorneAtaque.png", 12)}
    boss['parado'].set_total_duration(500)
    boss['correndo'].set_total_duration(500)
    boss['correndo'].set_position(100, 100)
    boss['atacando'].set_total_duration(600)
    boss['spriteAtual'] = boss['correndo']

    # setup obstáculos

    vetArvores = []

    for i in range(36):
        vetArvores.append(Sprite("Sprites/árvore_pequena.png"))

    vetArvores[0].set_position(200, 200)
    vetArvores[1].set_position(700, 500)
    vetArvores[2].set_position(1000, 300)
    vetArvores[3].set_position(500, 100)

    espelhoObstaculos(vetArvores, 4, janela)

    vetPedras = []

    for i in range(54):
        vetPedras.append(Sprite("Sprites/pedra1peq.png"))

    vetPedras[0].set_position(350, 250)
    vetPedras[1].set_position(850, 400)
    vetPedras[2].set_position(1000, 600)
    vetPedras[3].set_position(200, 700)
    vetPedras[4].set_position(500, 500)
    vetPedras[5].set_position(900, 100)

    espelhoObstaculos(vetPedras, 6, janela)

    vetPeca = [Sprite("Sprites/peçapequena.png")]

    # setup geral

    global cooldownDanoJ

    global nivelBip
    global nivelBumer
    global nivelLaser
    global nivelAmber
    cont_pausa = 0
    armadura = 1

    venceu = False

    tempo_de_jogo = 0

    nivelBip = 1
    nivelAmber = 0
    nivelBumer = 0
    nivelLaser = 0

    armadura = 1

    gameover = False

    # setup dos bips e zetas

    velBip = 80
    danoBip = 5

    tiroZeta = []
    velTzeta = 400
    danoZeta = 8
    velZeta = 90

    # setup cooldowns, timers e contadores

    cooldownB = 0
    cooldownSpawnBip = 0
    cooldownSpawnZeta = 0
    cooldownSpawnKaze = 0
    cooldownDanoJ
    cooldownA = 0
    cooldownBoss = 0

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
    aumentou = False

    # setup da bumerarma

    Bumerarma = {'sprite': Animation("Sprites/Bumerarma_animação.png", 3), 'ativo?': False, 'dx': 0, 'dy': 0, 'vel': 600, 'contador': 0, 'dano': 0, 'tempo': 1}
    Bumerarma['sprite'].set_total_duration(150)
    Bumerarma['sprite'].set_position(john['John'].x, john['John'].y)

    Summon = {'sprite': Animation("Sprites/Bumerarma_animação2.png", 3), 'ativo?': False, 'vel': 600, 'contador': 0, 'dano': 0}
    Summon['sprite'].set_total_duration(150)
    Summon['sprite'].set_position(john['John'].x, john['John'].y)


    mouseApertado = False

    Arma = 1

    # setup HUD

    # vida = Sprite("Sprites/9vidas.png")
    # vida.x = janela.width / 2 - vida.width / 2
    # vida.y = janela.height - vida.height - 25

    # vida
    lista_vida = [Sprite("Sprites/1vida.png"), Sprite("Sprites/2vidas.png"),
                  Sprite("Sprites/3vidas.png"), Sprite("Sprites/4vidas.png"),
                  Sprite("Sprites/5vidas.png"), Sprite("Sprites/6vidas.png"), Sprite("Sprites/7vidas.png"),
                  Sprite("Sprites/8vidas.png"), Sprite("Sprites/9vidas.png")]
    vida = lista_vida[(int(john['vida'] / 10)-2)]
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

    amber_lateral_2 = Sprite("Sprites/amber_lateral.png")
    amber_lateral_2.x = 10
    amber_lateral_2.y = 215 + 276

    bumerangue_lateral_2 = Sprite("Sprites/bumerangue_lateral(1).png")
    bumerangue_lateral_2.x = 10
    bumerangue_lateral_2.y = 185 + 92

    canhao_lateral_2 = Sprite("Sprites/canhao_lateral.png")
    canhao_lateral_2.x = 10
    canhao_lateral_2.y = 200 + 184

    balão = Sprite("Sprites/caixa de texto(1).png")
    balão.set_position(janela.width/2 - balão.width/2, janela.height - 230)

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

        if nivelBumer == 5:
            Summon['ativo?'] = True

        if nivelAmber >= 1:
            amber_lateral = amber_lateral_2

        if nivelBumer >= 1:
            bumerangue_lateral = bumerangue_lateral_2

        if nivelLaser >= 1:
            canhao_lateral = canhao_lateral_2

        # cooldowns e timers

        cooldownB -= (20 + (nivelBip * 2) ** 1.7) * janela.delta_time()
        cooldownSpawnBip -= 15 * janela.delta_time()
        cooldownSpawnZeta -= 1.5 * janela.delta_time()
        cooldownSpawnKaze -= 2 * janela.delta_time()
        cooldownDanoJ -= 15 * janela.delta_time()
        cooldownA -= 20 * janela.delta_time()
        cooldownBoss -= janela.delta_time()

        # velocidade de movimento do personagem

        velJohnX = 0
        velJohnY = 0

        if teclado.key_pressed('W'):
            velJohnY = 400

            if john['direcao'] == 1:
                john['John'] = johnCorrendo
            elif john['direcao'] == 2:
                john['John'] = johnCorrendoInv

            john['correndo?'] = True
        if teclado.key_pressed('A'):
            velJohnX = 400
            john['John'] = johnCorrendoInv
            john['correndo?'] = True
            john['direcao'] = 2
        if teclado.key_pressed('S'):
            velJohnY = -400

            if john['direcao'] == 1:
                john['John'] = johnCorrendo
            elif john['direcao'] == 2:
                john['John'] = johnCorrendoInv

            john['correndo?'] = True
        if teclado.key_pressed('D'):
            velJohnX = -400
            john['John'] = johnCorrendo
            john['correndo?'] = True
            john['direcao'] = 1

        if velJohnY == velJohnX == 0:
            if john['direcao'] == 1:
                john['John'] = johnParado
            elif john['direcao'] == 2:
                john['John'] = johnParadoInv
            john['correndo?'] = False

        velJohnX, velJohnY = colisãoPlayerCenario(vetArvores, john, velJohnX, velJohnY, janela)
        velJohnX, velJohnY = colisãoPlayerCenario(vetPedras, john, velJohnX, velJohnY, janela)

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

        for n in range(len(vetPedras)):
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
            ativaBumerangue(Mouse, Bumerarma, john['John'])
        elif Arma == 3:
            pass
        elif Arma == 4:
            if cooldownA <= 0:
                amberPode, cooldownA = tiroAmber(janela, vetAmber, Mouse, john['John'], velAmber, amberPode, cooldownA)
            if not amberPode:
                timerAmber += janela.delta_time()
                amberPode, timerAmber, aumentou = carregaAmber(amberPode, janela, vetAmber, Mouse, john['John'], timerAmber,
                                                     mouseApertado, velAmber, danoAmber, aumentou, nivelAmber)
            else:
                timerAmber = 0
                aumentou = False

        # colisão com dano

        colisãoDano(vetBip, vetBipper, vetAmber, danoBipper, Bumerarma, Summon)
        colisãoDano(vetZeta, vetBipper, vetAmber, danoBipper, Bumerarma, Summon)
        colisãoDano(vetKaze, vetBipper, vetAmber, danoBipper, Bumerarma, Summon)
        cooldownBoss = colisãoDanoBoss(boss, vetBipper, vetAmber, danoBipper, Bumerarma, john, Summon, cooldownBoss)

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
            zeta(vetZeta[i], janela, velJohnX, velJohnY, velZeta, john, tiroZeta)

        tirosZeta(tiroZeta, velTzeta, velJohnX, velJohnY, janela, john, danoZeta)

        # comportamento dos kazes

        if cooldownSpawnKaze <= 0:
            if tempo_de_jogo > 0:
                spawnKaze(vetKaze, janela)
            cooldownSpawnKaze = 10

        for i in range(len(vetKaze)):
            kaze(vetKaze[i][0], janela, velJohnX, velJohnY, velBip, john, danoBip, armadura)

        # verifica se algum bip está com vida < 0 e mata o que estiver

        morreuInimigo(vetBip, vetPeca, 20)
        morreuInimigo(vetZeta, vetPeca, 80)
        morreuInimigo(vetKaze, vetPeca, 50)

        # boss

        if tempo_de_jogo > 15*60+15 and not venceu:
            bossFunc(boss, janela, velJohnX, velJohnY, john)

        if boss['vida'] <= 0:
            venceu = True

        # renderizar tiros

        renderizarBipper(vetBipper, janela, velJohnX, velJohnY)
        colisãoTiroCenario(vetBipper, vetArvores)
        colisãoTiroCenario(vetBipper, vetPedras)

        renderizaAmber(vetAmber, velJohnX, velJohnY, janela, nivelAmber)
        bumerarma(Bumerarma, janela, Mouse, john['John'], velJohnX, velJohnY, Summon)

        # HUD
        vida = lista_vida[(ceil(john['vida'] / 10) - 1)]
        vida.x = janela.width / 2 - vida.width / 2
        vida.y = janela.height - vida.height - 25

        HUD(janela, john, pecas_hud, bipper_lateral, amber_lateral, bumerangue_lateral, canhao_lateral, vida, pausa,
            nivelBip, nivelAmber, nivelLaser, nivelBumer)

        tempo_de_jogo = tempo(janela, tempo_de_jogo)

        # niveis

        niveisDeArma(mouseApertado, john, Mouse, janela, bipper_lateral, bumerangue_lateral, amber_lateral, canhao_lateral)

        # sair

        cont_pausa += janela.delta_time()
        if (teclado.key_pressed('ESC') or (Mouse.is_over_area((pausa.x, pausa.y), (pausa.x + pausa.width, pausa.y + pausa.height)) and Mouse.is_button_pressed(1))) and cont_pausa >= 0.3:
            cont_pausa = 0
            res = menupausa(tempo_de_jogo, janela)
            if res == 1 or res == 2:
                break

        # game over

        if john['vida'] <= 0:
            gameover = True

        # auxilia pro mouse so clicar se estiver "desligado"

        if Mouse.is_button_pressed(1):
            mouseApertado = True
        else:
            mouseApertado = False

        # fps

        contador_fps += 1
        soma_fps += janela.delta_time()
        janela.draw_text('FPS: {}'.format(int(printfps)), janela.width - 100, janela.height - 30, 17,
                             (255, 255, 255))

        if contador_fps == 80:
            printfps = contador_fps / soma_fps
            contador_fps = 0
            soma_fps = 0

        # obstaculos

        posRel(posRelativa, janela, velJohnX, velJohnY)
        obsInfinitos(posRelativa, janela, vetArvores, vetPedras, john['John'])

        # atualizações

        if 15*60 <= tempo_de_jogo <= 15*60+15:
            balão.draw()

        if john['correndo?']:
            john['John'].play()
            john['John'].update()
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

        if len(vetAmber) > 0:
            print('{:.2f}'.format(vetAmber[-1][3]))
