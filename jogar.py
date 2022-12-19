from PPlay.sound import *
from PPlay.animation import *
from PPlay.sprite import *
from PPlay.window import *
from armas_funções import *
from outras_funções import *
from menu import *
from inimigos_funções import *
from math import ceil

nivelBip = 1
nivelAmber = 0
nivelBumer = 0
nivelLaser = 0

cooldownDanoJ = 0

def bip(Bip, janela, velJohnX, velJohnY, velBip, john, danoBip, armadura, half):

    global cooldownDanoJ

    Bip.x += velJohnX * janela.delta_time()
    Bip.y += velJohnY * janela.delta_time()
    if half == 0:
        dx = john['John'].x - Bip.x
        dy = john['John'].y - Bip.y
        dt = abs(dx) + abs(dy)
        Bip.x += velBip * (dx / dt) * janela.delta_time()
        Bip.y += velBip * (dy / dt) * janela.delta_time()
        if Bip.collided(john['John']) and cooldownDanoJ <= 0:
            john['vida'] -= danoBip * armadura
            cooldownDanoJ = 20
    Bip.draw()

def kaze(Kaze,timerExp, tocou, vetKaze, posicao, janela, velJohnX, velJohnY, velKaze, john, danoBip, armadura, half):

    global cooldownDanoJ
    Kaze.x += velJohnX * janela.delta_time()
    Kaze.y += velJohnY * janela.delta_time()
    dx = john['John'].x - Kaze.x
    dy = john['John'].y - Kaze.y
    dt = abs(dx) + abs(dy)
    Kaze.x += velKaze * (dx / dt) * janela.delta_time() * 2
    Kaze.y += velKaze * (dy / dt) * janela.delta_time() * 2
    RetJohn = Sprite("Sprites/vazio.png")
    RetJohn.x = janela.width/2 - RetJohn.width/2
    RetJohn.y = janela.height/2 - RetJohn.height/2
    explodiu = 0
    kazex = Kaze.x
    kazey = Kaze.y
    if Kaze.collided(RetJohn) and not tocou:
        tocou = 1
        timerExp -= 0.1
    if Kaze.collided(john['John']) and cooldownDanoJ <= 0:
        john['vida'] -= danoBip * 2 * armadura
        cooldownDanoJ = 20
        vetKaze.pop(posicao)
        explodiu = 1
        explosao = Sprite("Sprites/explosao.png")
        explosao.x = kazex
        explosao.y = kazey
        explosao.draw()
        som_explosao = Sound("Sons/som_kaze_exp.mp3")
        som_explosao.set_volume(10)
        som_explosao.play()
        return kazex, kazey, explodiu
    if tocou and timerExp != 3:
        valor = sin(pygame.time.get_ticks())
        if valor >= 0:
            Kaze.draw()
            timerExp -= 9*janela.delta_time()
        else:
            timerExp -= 9*janela.delta_time()
    else:
        Kaze.draw()
    return kazex, kazey, explodiu


def niveisDeArma(mouseApertado, john, Mouse, bipper_lateral, bumerangue_lateral, amber_lateral):

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
        elif nivelBip == 3 and john['pregos'] >= 25:
            john['pregos'] -= 25
            nivelBip = 4
        elif nivelBip == 4 and john['pregos'] >= 35:
            john['pregos'] -= 35
            nivelBip = 5

    if not mouseApertado and Mouse.is_button_pressed(1) and amber_lateral.x + amber_lateral.width - 20\
            < Mouse.get_position()[0] < amber_lateral.x + amber_lateral.width and amber_lateral.y\
            + amber_lateral.height - 20 < Mouse.get_position()[1] < amber_lateral.y + amber_lateral.height:
        if nivelAmber == 0 and john['pregos'] >= 5:
            john['pregos'] -= 5
            nivelAmber = 1
        elif nivelAmber == 1 and john['pregos'] >= 10:
            john['pregos'] -= 10
            nivelAmber = 2
        elif nivelAmber == 2 and john['pregos'] >= 15:
            john['pregos'] -= 15
            nivelAmber = 3
        elif nivelAmber == 3 and john['pregos'] >= 20:
            john['pregos'] -= 20
            nivelAmber = 4
        elif nivelAmber == 4 and john['pregos'] >= 30:
            john['pregos'] -= 30
            nivelAmber = 5

    if not mouseApertado and Mouse.is_button_pressed(1) and bumerangue_lateral.x + bumerangue_lateral.width - 20\
            < Mouse.get_position()[0] < bumerangue_lateral.x + bumerangue_lateral.width and bumerangue_lateral.y\
            + bumerangue_lateral.height - 20 < Mouse.get_position()[1] < bumerangue_lateral.y + bumerangue_lateral.height:
        if nivelBumer == 0 and john['pregos'] >= 5:
            john['pregos'] -= 5
            nivelBumer = 1
        elif nivelBumer == 1 and john['pregos'] >= 10:
            john['pregos'] -= 10
            nivelBumer = 2
        elif nivelBumer == 2 and john['pregos'] >= 15:
            john['pregos'] -= 15
            nivelBumer = 3
        elif nivelBumer == 3 and john['pregos'] >= 20:
            john['pregos'] -= 20
            nivelBumer = 4
        elif nivelBumer == 4 and john['pregos'] >= 30:
            john['pregos'] -= 30
            nivelBumer = 5


def jogar(teclado, Mouse, janela, mapa):
    while True:
        mapa.draw()
        janela.draw_text("Instruções Básicas", janela.width/2 - 220, 40 , 55, (255, 255, 255), "Candara")
        janela.draw_text("Movimentação  -  W  A  S  D  (Cima, Esquerda, Baixo e Direita)", 50, 150, 42, (255, 255, 255), "Candara")
        janela.draw_text("Atirar  -  Botão Esquerdo do Mouse", 50, 250, 42, (255, 255, 255), "Candara")
        janela.draw_text("Manual das Armas  -  G", 50, 350, 42, (255, 255, 255), "Candara")
        janela.draw_text("Pressione ESPAÇO para continuar", janela.width/2 - 300, 650, 42, (255,255,255), "Candara")
        janela.draw_text("Mate inimigos, colete peças metálicas e fortaleça suas armas!!!", 50, 440, 30, (200,200,200), "Candara")
        janela.draw_text("Clique no '+' no retrato da arma quando possuir peças para fortalece-la!", 50, 490, 30, (200, 200, 200), "Candara")
        janela.draw_text("Utilize 1, 2 e 3 para trocar de armas", 50, 540, 30, (200,200,200), "Candara")
        janela.draw_text("Sobreviva e evolua até a ajuda chegar...", 50, 590, 30, (200,200,200), "Candara")
        if teclado.key_pressed("SPACE"):
            break
        janela.update()

    # setup player

    half = 0
    half2 = 0
    otimização = 7  # quanto maior, menos travado porém mais tremedeira nas colisões dos inimigos
    otimização2 = 3

    john = {'John': Sprite("Sprites/Astronauta(3).png"), 'vida': 90, 'pregos': 0, 'correndo?': False, 'direcao': 1}
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

    velJ = 400 * otimização / 4

    # setup inimigos

    vetBip = []

    vetZeta = []

    vetKaze = []

    boss = {'spriteAtual': 0, 'vida': 2200, 'dano': 35, 'dash': False, 'primeiro': False, 'velDash': 1500, 'cooldownDash': 0.5, 'pausa':False,  'alvo': 0, 'cooldown': 0, 'parado': Animation("Sprites/boss_parado.png", 9), 'correndo': Animation("Sprites/correndoVetor.png", 6), 'atacando': Animation("Sprites/NightBorneAtaque.png", 12)}
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

    espelhoObstaculos(vetPedras, 6, janela) # faz com que os obstáculos sejam infinitos

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

    gameover = False

    # setup dos bips e zetas

    velBip = 80 * otimização2
    velKaze = 80
    danoBip = 5

    tiroZeta = []
    velTzeta = 400
    danoZeta = 8
    velZeta = 90 * otimização2

    # setup cooldowns, timers e contadores

    cooldownCheck = 0.1

    cooldownB = 0
    cooldownSpawnBip = 0
    cooldownSpawnZeta = 1740
    cooldownSpawnKaze = 870
    cooldownDanoJ
    cooldownA = 0
    cooldownBoss = 0
    cooldownTroca = 0
    timerExpKaze = 0
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

    vitoria = Sprite("Sprites/Venceu.png")

    # vida
    lista_vida = [Sprite("Sprites/1vida.png"), Sprite("Sprites/2vidas.png"),
                  Sprite("Sprites/3vidas.png"), Sprite("Sprites/4vidas.png"),
                  Sprite("Sprites/5vidas.png"), Sprite("Sprites/6vidas.png"), Sprite("Sprites/7vidas.png"),
                  Sprite("Sprites/8vidas.png"), Sprite("Sprites/9vidas.png")]

    bipper_lateral = Sprite("Sprites/bipper_lateral.png")
    bipper_lateral.x = 10
    bipper_lateral.y = 170
    bumerangue_lateral = Sprite("Sprites/bumerangue_lateral_desabilitado.png")
    bumerangue_lateral.x = 10
    bumerangue_lateral.y = bipper_lateral.y + bumerangue_lateral.height + 15
    amber_lateral = Sprite("Sprites/amber_lateral_desabilitada.png")
    amber_lateral.x = 10
    amber_lateral.y = bumerangue_lateral.y + bumerangue_lateral.height + 15
    pausa = Sprite("Sprites/pausa.png")
    pausa.x = 10
    pausa.y = 10
    pecas_hud = Sprite("Sprites/uma peça.png")
    pecas_hud.x = janela.width - pecas_hud.width - 30
    pecas_hud.y = 15

    amber_lateral_2 = Sprite("Sprites/amber_lateral.png")
    amber_lateral_2.x = amber_lateral.x
    amber_lateral_2.y = amber_lateral.y

    bumerangue_lateral_2 = Sprite("Sprites/bumerangue_lateral(1).png")
    bumerangue_lateral_2.x = bumerangue_lateral.x
    bumerangue_lateral_2.y = bumerangue_lateral.y

    balão = Sprite("Sprites/caixa de texto(1).png")
    balão.set_position(janela.width/2 - balão.width/2, janela.height - 230)

    # fps

    soma_fps = 0
    contador_fps = 0
    printfps = 0

    som_jogo = Sound("Sons/lifelike.mp3")
    som_jogo.set_volume(8)
    som_jogo.set_repeat(1)
    som_jogo.play()

    som_boss = Sound("Sons/som_boss.mp3")
    som_boss.set_volume(10)
    som_boss.set_repeat(1)
    som_boss_on = 0

    # Game loop

    while True:

        '''if Mouse.is_button_pressed(3):
            velJ = 200
        else:
            velJ = 40'''

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

        '''if nivelBumer == 3:
            Bumerarma['sprite'] = Animation("Sprites/Bumerarma_animação(3).png", 3)
            Bumerarma['sprite'].set_total_duration(150)
            Bumerarma['sprite'].set_position(john['John'].x, john['John'].y)'''

        if nivelBumer == 3:
            Bumerarma['vel'] = 800
            Bumerarma['tempo'] = 0.8
        if nivelBumer == 5:
            Bumerarma['vel'] = 1000
            Bumerarma['tempo'] = 0.7


        # cooldowns e timers

        cooldownCheck -= janela.delta_time()

        cooldownB -= (20 + (nivelBip * 2) ** 1.7) * janela.delta_time()
        cooldownSpawnBip -= 15 * janela.delta_time()
        cooldownSpawnZeta -= 15 * janela.delta_time()
        cooldownSpawnKaze -= 15 * janela.delta_time()
        cooldownDanoJ -= 15 * janela.delta_time()
        cooldownA -= 20 * janela.delta_time()
        cooldownBoss -= janela.delta_time()

        # velocidade de movimento do personagem

        velJohnX = 0
        velJohnY = 0

        if half == 0 or half == int(otimização / 4) or half == 2*int(otimização / 4) or half == 3*int(otimização / 4):

            if teclado.key_pressed('W'):
                velJohnY = velJ

                if john['direcao'] == 1:
                    john['John'] = johnCorrendo
                elif john['direcao'] == 2:
                    john['John'] = johnCorrendoInv

                john['correndo?'] = True
            if teclado.key_pressed('A'):
                velJohnX = velJ
                john['John'] = johnCorrendoInv
                john['correndo?'] = True
                john['direcao'] = 2
            if teclado.key_pressed('S'):
                velJohnY = -velJ

                if john['direcao'] == 1:
                    john['John'] = johnCorrendo
                elif john['direcao'] == 2:
                    john['John'] = johnCorrendoInv

                john['correndo?'] = True
            if teclado.key_pressed('D'):
                velJohnX = -velJ
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
        elif teclado.key_pressed('3') and nivelAmber >= 1:
            Arma = 3

        if Arma == 1:
            # criação de pojeteis da bipper
            cooldownB = tiroBipper(janela, Mouse, john['John'], velTiro, vetBipper, cooldownB)
        elif Arma == 2:
            ativaBumerangue(Mouse, Bumerarma, john['John'])
        elif Arma == 3:
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
        if cooldownCheck <= 0:
            colisãoDano(vetBip, vetBipper, vetAmber, danoBipper, Bumerarma, Summon)
            colisãoDano(vetZeta, vetBipper, vetAmber, danoBipper, Bumerarma, Summon)
            colisãoDano(vetKaze, vetBipper, vetAmber, danoBipper, Bumerarma, Summon)
        cooldownBoss = colisãoDanoBoss(boss, vetBipper, vetAmber, danoBipper, Bumerarma, john, Summon, cooldownBoss)

        # comportamento dos bips

        if cooldownSpawnBip <= 0 and len(vetBip) <= 35:
            spawnBip(vetBip, janela)
            cooldownSpawnBip = 25


        for i in range(len(vetBip)):
            bip(vetBip[i][0], janela, velJohnX, velJohnY, velBip, john, danoBip, armadura, half2)

        # comportamento dos zetas

        if cooldownSpawnZeta <= 0 and len(vetZeta) <= 10:
            if tempo_de_jogo > 0:
                spawnZeta(vetZeta, janela)
            cooldownSpawnZeta = 250

        for i in range(len(vetZeta)):
            zeta(vetZeta[i], janela, velJohnX, velJohnY, velZeta, john, tiroZeta, half2)

        tirosZeta(tiroZeta, velTzeta, velJohnX, velJohnY, janela, john, danoZeta)

      # comportamento dos kazes

        if cooldownSpawnKaze <= 0 and len(vetKaze) <= 5:
            if tempo_de_jogo > 0:
                spawnKaze(vetKaze, janela)
            cooldownSpawnKaze = 45

        for i in range(len(vetKaze)):
            kazex = 0
            kazey = 0
            kazex, kazey, explodiu = kaze(vetKaze[i][0],vetKaze[i][2], vetKaze[i][3], vetKaze, i, janela, velJohnX, velJohnY, velKaze, john, danoBip, armadura, half)
            if explodiu:
                break

        # verifica se algum bip está com vida < 0 e mata o que estiver
        if cooldownCheck <= 0:
            morreuInimigo(vetBip, vetPeca, 50)
            morreuInimigo(vetZeta, vetPeca, 100)
            morreuInimigo(vetKaze, vetPeca, 70)

        # boss

        if tempo_de_jogo > 10*60+15 and not venceu:
            if som_jogo.is_playing():
                som_jogo.stop()
            if not som_boss_on:
                som_boss.play()
                som_boss_on = 1
            bossFunc(boss, janela, velJohnX, velJohnY, john)

        if boss['vida'] <= 0 and not venceu:
            venceu = True
            tempoVitoria = tempo_de_jogo

        if venceu and tempo_de_jogo > tempoVitoria + 3:
            while True:
                janela.set_background_color([0, 0, 0])
                vitoria.draw()
                janela.draw_text('Aperte ESC para voltar ao menu principal', janela.width - 550, janela.height - 30, 30,
                                 (255, 255, 255), "Candara")
                janela.update()
                if teclado.key_pressed('ESC'):
                    break
            break


        # atualizar tiros

        atualizaBipper(vetBipper, janela, velJohnX, velJohnY)
        if cooldownCheck <= 0:
            colisãoTiroCenario(vetBipper, vetArvores)
            colisãoTiroCenario(vetBipper, vetPedras)

        atualizaAmber(vetAmber, velJohnX, velJohnY, janela, nivelAmber)
        bumerarma(Bumerarma, janela, Mouse, john['John'], velJohnX, velJohnY, Summon, nivelBumer)

        # HUD

        if john['vida'] > 90:    # para testes
            vida = lista_vida[3]
            vida.x = janela.width / 2 - vida.width / 2
            vida.y = janela.height - vida.height - 25
        if john['vida'] <= 90:
            vida = lista_vida[(ceil(john['vida'] / 10) - 1)]
            vida.x = janela.width / 2 - vida.width / 2
            vida.y = janela.height - vida.height - 25
        troca_prego_vida = Sprite("Sprites/prego_vida.png")
        troca_prego_vida.x = vida.x + vida.width + 15
        troca_prego_vida.y = vida.y - 20
        troca_prego_vida.draw()

        if john['vida'] <= 80:
            if Mouse.is_over_area((troca_prego_vida.x, troca_prego_vida.y), (troca_prego_vida.x + troca_prego_vida.width, troca_prego_vida.y + troca_prego_vida.height)) and Mouse.is_button_pressed(1) and cooldownTroca <= 0 and john['pregos'] >= 15 and not mouseApertado:
                john['pregos'] -= 15
                john['vida'] += 10
                cooldownTroca = 1.5
        if cooldownTroca >= 0:
            cooldownTroca -= janela.delta_time()

        HUD(janela, john, pecas_hud, bipper_lateral, amber_lateral, bumerangue_lateral, vida, pausa,
            nivelBip, nivelAmber, nivelBumer)

        tempo_de_jogo = tempo(janela, tempo_de_jogo)

        # niveis

        niveisDeArma(mouseApertado, john, Mouse, bipper_lateral, bumerangue_lateral, amber_lateral)

        # sair

        cont_pausa += janela.delta_time()
        if (teclado.key_pressed('ESC') or (Mouse.is_over_area((pausa.x, pausa.y), (pausa.x + pausa.width, pausa.y + pausa.height)) and Mouse.is_button_pressed(1))) and cont_pausa >= 0.3:
            som_clique = Sound("Sons/som_clique.mp3")
            som_clique.set_volume(20)
            som_clique.play()
            cont_pausa = 0
            res = menupausa(tempo_de_jogo, janela)
            if res == 1 or res == 2:
                mouseApertado = True
                break
        if teclado.key_pressed('G'):
            menu_armas(tempo_de_jogo, janela)

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
        if printfps < 60:
            erro = 2 * otimização
        else:
            erro = 5 * otimização
        if half == 0:
            colisao_inimigo_cenario(vetBip, vetArvores, vetPedras, velBip, john, janela, erro)
            colisao_inimigo_cenario(vetKaze, vetArvores, vetPedras, 2*velBip, john, janela, erro)
            colisao_inimigo_cenario(vetZeta, vetArvores, vetPedras, velBip, john, janela, erro)

        if 10*60 <= tempo_de_jogo <= 10*60+15:
            balão.draw()

        if john['correndo?']:
            john['John'].play()
            john['John'].update()
        john['John'].draw()
        janela.update()

        if cooldownCheck <= 0:
            cooldownCheck = 0.01

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

        half += 1
        if half >= otimização:
            half = 0

        half2 += 1
        if half2 >= otimização2:
            half2 = 0

        if printfps < 60:
            otimização = 4
            otimização2 = 3
            velJ = 400 * otimização / 4
        else:
            otimização = 1
            otimização2 = 1
            velJ = 400 * otimização

        velBip = 80 * otimização2
        velZeta = 80 * otimização2

    return mouseApertado
