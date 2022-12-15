from random import randint
from outras_funções import areaSpawn
from PPlay.sprite import *
from jogar import *
from armas_funções import *
from outras_funções import *
from PPlay.animation import *
from menu import *
from math import ceil


def zeta(Zeta, janela, velJohnX, velJohnY, velZeta, john, tiroZeta):

    Zeta[0].x += velJohnX * janela.delta_time()
    Zeta[0].y += velJohnY * janela.delta_time()
    dx = john['John'].x - Zeta[0].x
    dy = john['John'].y - Zeta[0].y
    dt = abs(dx) + abs(dy)
    if dx ** 2 + dy ** 2 > 200 ** 2:
        Zeta[0].x += velZeta * (dx / dt) * janela.delta_time()
        Zeta[0].y += velZeta * (dy / dt) * janela.delta_time()

    if Zeta[2] <= 0:
        tiroZeta.append({'sprite': Sprite("Sprites/Zeta-projetil.png"), 'dx': dx / dt, 'dy': dy / dt})
        tiroZeta[-1]['sprite'].set_position(Zeta[0].x, Zeta[0]. y)
        Zeta[2] = 20

    Zeta[2] -= 5 * janela.delta_time()

    Zeta[0].draw()

def tirosZeta(tiroZeta, velTzeta, velJohnX, velJohnY, janela, john, danoZeta):

    for i in tiroZeta:
        i['sprite'].x += (velJohnX + i['dx'] * velTzeta) * janela.delta_time()
        i['sprite'].y += (velJohnY + i['dy'] * velTzeta) * janela.delta_time()
        i['sprite'].draw()

    for i in range(len(tiroZeta)):
        if tiroZeta[i]['sprite'].collided(john['John']):
            tiroZeta.pop(i)
            john['vida'] -= danoZeta
            break

    for i in range(len(tiroZeta)):
        if tiroZeta[i]['sprite'].x < 0 or tiroZeta[i]['sprite'].x > janela.width or tiroZeta[i]['sprite'].y < 0 or tiroZeta[i][
            'sprite'].y > janela.height:
            tiroZeta.pop(i)
            break


def bossFunc(boss, janela, velJohnX, velJohnY, john):

    boss['cooldown'] -= janela.delta_time()

    velBoss1 = 500

    if boss['spriteAtual'].y > john['John'].y:
        velBoss1 = -500

    if boss['cooldown'] <= 0 and (-1 <= (boss['spriteAtual'].y - john['John'].y) <= 1) and not boss['dash']:
        boss['dash'] = True
        boss['atacando'].set_position(boss['spriteAtual'].x - 20, boss['spriteAtual'].y - 50)
        boss['spriteAtual'] = boss['atacando']
        boss['alvo'] = john['John'].x

        if boss['spriteAtual'].x > boss['alvo']:
            boss['velDash'] = -1800
        else:
            boss['velDash'] = 1800

    if boss['dash']:
        boss['spriteAtual'].x += boss['velDash'] * janela.delta_time()
        if (-50 <= boss['spriteAtual'].x - boss['alvo'] <= 50 and boss['velDash'] > 0) or (-50 <= boss['spriteAtual'].x
                                                                                           + boss['spriteAtual'].width -
                                                                                           boss['alvo'] <= 50 and
                                                                                           boss['velDash'] < 0):
            boss['dash'] = False
            boss['cooldown'] = 2
            boss['parado'].set_position(boss['spriteAtual'].x + 20, boss['spriteAtual'].y + 50)
            boss['spriteAtual'] = boss['parado']

    boss['spriteAtual'].x += velJohnX * janela.delta_time()
    boss['spriteAtual'].y += velJohnY * janela.delta_time()
    if not boss['dash'] and boss['cooldown'] <= 0:
        boss['correndo'].set_position(boss['spriteAtual'].x, boss['spriteAtual'].y)
        boss['spriteAtual'] = boss['correndo']
        boss['spriteAtual'].y += velBoss1 * janela.delta_time()
    boss['spriteAtual'].update()
    boss['spriteAtual'].draw()


def colisãoDanoBoss(inimigo, tiroB, tiroA, danoB, Bumerarma, john, Summon, cooldown):

    for j in tiroB:
        if inimigo['spriteAtual'].collided(j[0]):
            inimigo['vida'] -= danoB
    for j in tiroA:
        if inimigo['spriteAtual'].collided(j[0]) and j[5]:
            inimigo['vida'] -= j[3]
            j[4] += 1
    if Bumerarma['sprite'].collided(inimigo['spriteAtual']):
        inimigo['vida'] -= Bumerarma['dano']
    if Summon['sprite'].collided(inimigo['spriteAtual']):
        inimigo['vida'] -= Summon['dano']

    for j in range(len(tiroB)):
        if tiroB[j][0].collided(inimigo['spriteAtual']):
            tiroB.pop(j)
            break

    if john['John'].collided(inimigo['spriteAtual']) and cooldown <= 0:
        john['vida'] -= inimigo['dano']
        cooldown = 1

    return cooldown

def morreuInimigo(inimigo, vetPeca, droprate):
    j = 0
    a = len(inimigo)
    while j < a and a > 0:
        if inimigo[j][1] <= 0:
            r = randint(1, 100)
            if r <= droprate:
                vetPeca.append(Sprite("Sprites/peçapequena.png"))
                vetPeca[-1].set_position(inimigo[j][0].x + inimigo[j][0].width / 2, inimigo[j][0].y + inimigo[j][0].height / 2)
            inimigo.pop(j)
            a -= 1
        j += 1


def spawnBip(vetBip, janela):

    x, y = areaSpawn(janela)

    vetBip.append([Sprite("Sprites/bip.png"), 30])
    vetBip[-1][0].set_position(x, y)


def spawnZeta(vetZeta, janela):

    x, y = areaSpawn(janela)

    vetZeta.append([Sprite("Sprites/zeta.png"), 120, 0])
    vetZeta[-1][0].set_position(x, y)

def spawnKaze(vetKaze, janela):

    x, y = areaSpawn(janela)

    vetKaze.append([Sprite("Sprites/kaze2.png"), 15, 3, 0])
    vetKaze[-1][0].set_position(x, y)

def colisao_inimigo_cenario(vetInimigo, vetArvore, vetPedra, velIni, john, janela):

    for i in range(len(vetInimigo)):
        dx = john['John'].x - vetInimigo[i][0].x
        dy = john['John'].y - vetInimigo[i][0].y
        dt = abs(dx) + abs(dy)
        velinix = velIni * (dx / dt) * janela.delta_time()
        veliniy = velIni * (dy / dt) * janela.delta_time()
        for n in range(len(vetArvore)):
            colidiu = 0
            if vetArvore[n].x > -100 and vetArvore[n].x < janela.width + 100 and vetArvore[n].y > -100 and vetArvore[n].y < janela.height + 100:
                if vetInimigo[i][0].x > -100 and vetInimigo[i][0].x < janela.width +100 and vetInimigo[i][0].y > -100 and vetInimigo[i][0].y < janela.height + 100:
                    if vetInimigo[i][0].collided(vetArvore[n]):
                        colidiu = 1
                    if colidiu:
                        if vetInimigo[i][0].x + vetInimigo[i][0].width + 3 > vetArvore[n].x and vetInimigo[i][0].x + vetInimigo[i][0].width - 3 < vetArvore[n].x:
                            vetInimigo[i][0].y += veliniy
                            vetInimigo[i][0].x -= velinix
                        elif vetInimigo[i][0].x - 3 < vetArvore[n].x + vetArvore[n].width and vetInimigo[i][0].x + 3 > vetArvore[n].x + vetArvore[n].width:
                            vetInimigo[i][0].y += veliniy
                            vetInimigo[i][0].x -= velinix
                        elif vetInimigo[i][0].y + vetInimigo[i][0].height + 3 > vetArvore[n].y and vetInimigo[i][0].y + vetInimigo[i][0].height - 3 < vetArvore[n].y:
                            vetInimigo[i][0].y -= veliniy
                            vetInimigo[i][0].x += velinix
                        elif vetInimigo[i][0].y - vetArvore[n].height - 3 < vetArvore[n].y and vetInimigo[i][0].y - vetArvore[n].height + 3 > vetArvore[n].y:
                            vetInimigo[i][0].y -= veliniy
                            vetInimigo[i][0].x += velinix
        for n in range(len(vetPedra)):
            colidiu = 0
            if vetPedra[n].x > -100 and vetPedra[n].x < janela.width + 100 and vetPedra[n].y > -100 and vetPedra[n].y < janela.height + 100:
                if vetInimigo[i][0].x > -100 and vetInimigo[i][0].x < janela.width + 100 and vetInimigo[i][0].y > -100 and vetInimigo[i][0].y < janela.height + 100:
                    if vetInimigo[i][0].collided(vetPedra[n]):
                        colidiu = 1
                    if colidiu:
                        if vetInimigo[i][0].x + vetInimigo[i][0].width + 3 > vetPedra[n].x and vetInimigo[i][0].x + vetInimigo[i][0].width - 3 < vetPedra[n].x:
                            vetInimigo[i][0].y += veliniy
                            vetInimigo[i][0].x -= velinix
                        elif vetInimigo[i][0].x - 3 < vetPedra[n].x + vetPedra[n].width and vetInimigo[i][0].x + 3 > vetPedra[n].x + vetPedra[n].width:
                            vetInimigo[i][0].y += veliniy
                            vetInimigo[i][0].x -= velinix
                        elif vetInimigo[i][0].y + vetInimigo[i][0].height + 3 > vetPedra[n].y and vetInimigo[i][0].y + vetInimigo[i][0].height - 3 < vetPedra[n].y:
                            vetInimigo[i][0].y -= veliniy
                            vetInimigo[i][0].x += velinix
                        elif vetInimigo[i][0].y - vetPedra[n].height - 3 < vetPedra[n].y and vetInimigo[i][0].y - vetPedra[n].height + 3 > vetPedra[n].y:
                            vetInimigo[i][0].y -= veliniy
                            vetInimigo[i][0].x += velinix

            """if colidiu and (vetInimigo[i][0].x + vetInimigo[i][0].width + 2 > vetArvore[n].x and vetInimigo[i][0].x + vetInimigo[i][0].width - 2 <= vetArvore[n].x):
                vetInimigo[i][0].y += veliniy
                vetInimigo[i][0].x -= velinix
                print('2')
            elif colidiu and (vetInimigo[i][0].x - vetArvore[n].width + 2 > vetArvore[n].x and vetInimigo[i][0].x - vetArvore[n].width - 2 <= vetArvore[n].x):
                vetInimigo[i][0].y += veliniy
                vetInimigo[i][0].x -= velinix
                print('1')
            elif colidiu and (vetInimigo[i][0].y + vetInimigo[i][0].height - 2 < vetArvore[n].y and vetInimigo[i][0].y + vetInimigo[i][0].height + 2 > vetArvore[n].y):
                vetInimigo[i][0].y -= veliniy
                vetInimigo[i][0].x += velinix
                print('aaaa')
            elif colidiu and (vetInimigo[i][0].y - vetArvore[n].height - 2 < vetArvore[n].y and vetInimigo[i][0].y - vetArvore[n].height + 2 > vetArvore[n].y):
                vetInimigo[i][0].y -= veliniy
                vetInimigo[i][0].x += velinix
                print('bbbb')"""