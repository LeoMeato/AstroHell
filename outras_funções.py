def HUD(janela, john, pecas_hud, bipper_lateral, amber_lateral, bumerangue_lateral, canhao_lateral, vida, pausa,
        nivelBip, nivelAmber, nivelBumer, nivelLaser):

    janela.draw_text("" + str(john['pregos']), pecas_hud.x - pecas_hud.width, 17, 40, (255, 255, 255), "Candara")

    janela.draw_text('{}'.format(nivelBip), bipper_lateral.x + bipper_lateral.width + 25,
                     bipper_lateral.y + bipper_lateral.height / 2, size=40, color=(255, 255, 255),
                     font_name="Candara")
    janela.draw_text('{}'.format(nivelAmber), amber_lateral.x + amber_lateral.width + 25,
                     amber_lateral.y + amber_lateral.height / 2, size=40, color=(255, 255, 255),
                     font_name="Candara")
    janela.draw_text('{}'.format(nivelBumer), canhao_lateral.x + canhao_lateral.width + 25,
                     canhao_lateral.y + canhao_lateral.height / 2, size=40, color=(255, 255, 255),
                     font_name="Candara")
    janela.draw_text('{}'.format(nivelLaser), bumerangue_lateral.x + bumerangue_lateral.width + 25,
                     bumerangue_lateral.y + bumerangue_lateral.height / 2, size=40, color=(255, 255, 255),
                     font_name="Candara")

    janela.draw_text('HP: {}'.format(john['vida']), vida.x + vida.width / 2 - 40, vida.y - 30, 30, (255, 255, 255),
                     "Candara")

    pausa.draw()
    pecas_hud.draw()
    amber_lateral.draw()
    canhao_lateral.draw()
    vida.draw()
    bumerangue_lateral.draw()
    bipper_lateral.draw()


def tempo(janela, tempo_de_jogo):
    tempo_de_jogo += janela.delta_time()
    tempo_de_jogo_min = tempo_de_jogo // 60
    tempo_de_jogo_seg = tempo_de_jogo - tempo_de_jogo_min * 60
    janela.draw_text("{}:{:0>2}".format(int(tempo_de_jogo_min), int(tempo_de_jogo_seg)), janela.width / 2 - 20, 17, 40,
                     (255, 255, 255), "Candara")
    return tempo_de_jogo


def posRel(posRelativa, janela, velJohnX, velJohnY):
    posRelativa[0] += velJohnX * janela.delta_time()
    posRelativa[1] += velJohnY * janela.delta_time()


def obsInfinitos(posRelativa, janela, vetArvores, vetPedras, John):

    if posRelativa[0] <= John.x - janela.width:
        for v in vetArvores:
            v.x += janela.width
        for v in vetPedras:
            v.x += janela.width
        posRelativa[0] = John.x
    elif posRelativa[0] + John.width >= John.x + janela.width:
        for v in vetArvores:
            v.x -= janela.width
        for v in vetPedras:
            v.x -= janela.width
        posRelativa[0] = John.x
    elif posRelativa[1] <= John.y - janela.height:
        for v in vetArvores:
            v.y += janela.height
        for v in vetPedras:
            v.y += janela.height
        posRelativa[1] = John.y
    elif posRelativa[1] >= John.y + janela.height:
        for v in vetArvores:
            v.y -= janela.height
        for v in vetPedras:
            v.y -= janela.height
        posRelativa[1] = John.y
