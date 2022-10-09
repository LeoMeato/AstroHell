def menu(BotaoJogar, BotaoConfiguraçoes, BotaoSair, Logo, Mouse, janela):
    resposta = 0
    Logo.draw()
    BotaoJogar.draw()
    BotaoConfiguraçoes.draw()
    BotaoSair.draw()
    if Mouse.is_button_pressed(1) and janela.width/2 - BotaoJogar.width/2 <= Mouse.get_position()[0] <= janela.width/2 + BotaoJogar.width/2:
        if BotaoJogar.y <= Mouse.get_position()[1] <= BotaoJogar.y + BotaoJogar.height:
            resposta = 1
        elif BotaoConfiguraçoes.y <= Mouse.get_position()[1] <= BotaoConfiguraçoes.y + BotaoConfiguraçoes.height:
            resposta = 2
        elif BotaoSair.y <= Mouse.get_position()[1] <= BotaoSair.y + BotaoSair.height:
            resposta = 3
    while Mouse.is_button_pressed(1):
        janela.update()
    return resposta