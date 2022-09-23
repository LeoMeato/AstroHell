from PPlay.window import *
from PPlay.sprite import *


def bolaQuica(obj, vel):
    if obj.y + obj.height >= 720:
        vel = -vel
        obj.y = 720 - obj.height
    if obj.y <= 0:
        vel = -vel
        obj.y = 0
    return vel


def moveBola(obj, velx, vely):
    obj.x = obj.x + velx * janela.delta_time()
    obj.y = obj.y + vely * janela.delta_time()


janela = Window(1220, 720)
janela.set_title("Pong")

bola = Sprite("img_20220909_095910291.png")
bola.set_position(565, 315)

bola2 = Sprite("img_20220909_095910291.png")
bola2.set_position(565, 315)

janela.set_background_color([255, 255, 255])

# velocidade da bola
velx = 1000
vely = 1000

# velocidade da bola 2
vel2x = 1000
vel2y = 1000

# velocidade dos pads
velty = 400

# velocidade do pad 2 controlado pela IA
velia = 400

pad1 = Sprite("Picsart_22-09-16_10-26-39-219.jpg")
pad2 = Sprite("Picsart_22-09-16_10-26-39-219.jpg")
pad1.set_position(30, 720/2 - pad1.height/2)
pad2.set_position(1190 - pad2.width/2, 720/2 - pad2.height/2)

teclado = Window.get_keyboard()

txt1 = Sprite("img_20220916_134356509.png")
txt1.set_position(1220/2 - txt1.width/2, 600)

contador1 = 0

p1 = p2 = 0

rebateu = 0

passou1 = passou2 = False

while(True):

    # Contadores da IA

    if contador1 > 0:
        contador1 -= 1

    # Fez ponto, trava até apertar espaço

    passou1 = bola.x >= 1220 or bola.x + bola.width <= 0
    passou2 = bola2.x >= 1220 or bola2.x + bola2.width <= 0

    if passou1 or passou2:
        if bola.x >= 1220 or bola2.x >= 1220:
            p1 += 1
        if bola.x + bola.width <= 0 or bola2.x + bola.width <= 0:
            p2 += 1

    if passou1 and rebateu < 3:
        bola.set_position(565, 315)
        bola.draw()
        while not teclado.key_pressed("SPACE"):
            txt1.draw()
            janela.update()

    # Bola quica

    vely = bolaQuica(bola, vely)

    janela.set_background_color([255, 255, 255])

    moveBola(bola, velx, vely)

    # Segunda bola

    if rebateu >= 3:
        vel2y = bolaQuica(bola2, vel2y)
        moveBola(bola2, vel2x, vel2y)
        bola2.draw()

        if pad1.collided(bola2):
            vel2x = -vel2x
            bola2.x = pad1.x + pad1.width
        if pad2.collided(bola2):
            vel2x = -vel2x
            bola2.x = pad2.x - bola2.width

        if passou1:
            bola.x = bola2.x
            bola.y = bola2.y
            velx = vel2x
            vely = vel2y
            rebateu = 0
        elif passou2:
            bola2.set_position(565, 315)
            rebateu = 0

    # Movimentação do pad 2 (player)

    '''if teclado.key_pressed("UP"):
        pad2.y -= velty * janela.delta_time()
    if teclado.key_pressed("DOWN"):
        pad2.y += velty * janela.delta_time()'''

    # Movimentação do pad2 (IA)

    if bola.collided(pad2):
        contador1 += 100

    if abs(bola.x - pad2.x) < abs(bola2.x - pad2.x) or rebateu < 3:

        if contador1 == 0:
            if pad2.y + pad2.height / 2 <= bola.y:
                velia = abs(velia)
            pad2.y += velia * janela.delta_time()

            if pad2.y + pad2.height / 2 >= bola.y:
                velia = -abs(velia)
            pad2.y += velia * janela.delta_time()

    else:

        if contador1 == 0:
            if pad2.y + pad2.height / 2 <= bola2.y:
                velia = abs(velia)
            pad2.y += velia * janela.delta_time()

            if pad2.y + pad2.height / 2 >= bola2.y:
                velia = -abs(velia)
            pad2.y += velia * janela.delta_time()

    # Movimentação do pad 1

    if teclado.key_pressed("W"):
        pad1.y -= velty * janela.delta_time()
    if teclado.key_pressed("S"):
        pad1.y += velty * janela.delta_time()

    # Colisão

    if pad1.collided(bola):
        velx = -velx
        bola.x = pad1.x + pad1.width
        rebateu += 1
    if pad2.collided(bola):
        velx = -velx
        bola.x = pad2.x - bola.width
        rebateu += 1

    # Limitação dos pads

    if pad1.y + pad1.height >= 720:
        pad1.y = 720 - pad1.height
    if pad1.y <= 0:
        pad1.y = 0

    if pad2.y + pad2.height >= 720:
        pad2.y = 720 - pad2.height
    if pad2.y <= 0:
        pad2.y = 0

    txt = "{} x {}".format(p1, p2)
    janela.draw_text(txt, 610 - 55, 115, size=50)

    bola.draw()
    pad1.draw()
    pad2.draw()
    janela.update()
