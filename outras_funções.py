def HUD(janela, john, pecas_hud, bipper_lateral, amber_lateral, bumerangue_lateral, canhao_lateral, vida, pausa,
        nivelBip, nivelAmber, nivelBumer, nivelLaser):

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

    janela.draw_text('HP: {}'.format(john['vida']), vida.x + vida.width / 2 - 40, vida.y - 30, 30, (255, 255, 255),
                     "Candara")

    pausa.draw()
    pecas_hud.draw()
    amber_lateral.draw()
    canhao_lateral.draw()
    vida.draw()
    bumerangue_lateral.draw()
    bipper_lateral.draw()