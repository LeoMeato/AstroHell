def menu(BotaoJogar, BotaoConfiguraçoes, BotaoSair, Mouse, janela, logo):
    resposta = 0
    logo.draw()
    BotaoJogar.draw()
    BotaoConfiguraçoes.draw()
    BotaoSair.draw()
    if Mouse.is_button_pressed(1) and janela.width/2 - BotaoJogar.width/2 <= Mouse.get_position()[0] <= janela.width/2 + BotaoJogar.width/2:
        if janela.height/2 - 300 <= Mouse.get_position()[1] <= janela.height/2 - 100 + BotaoJogar.height:
            resposta = 1
        elif janela.height/2 - 150 <= Mouse.get_position()[1] <= janela.height/2 + 50 + BotaoConfiguraçoes.height:
            resposta = 2
        elif janela.height/2 + 150 <= Mouse.get_position()[1] <= janela.height/2 + 200 + BotaoSair.height:
            resposta = 3
    while Mouse.is_button_pressed(1):
        janela.update()
    return resposta