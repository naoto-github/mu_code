# -*- coding: cp932 -*-

from random import *

WIDTH = 640 # �E�B���h�E�̕�
HEIGHT = 480 # �E�B���h�E�̍���

def draw():
    screen.fill("white")

    screen.blit("tree1", (0, 0))
    screen.blit("tree2", (300, 0))

    for i in range(3):
        x = randint(100, 240)
        y = randint(60, 200)
        screen.draw.filled_circle((x, y), 10, (255, 0, 0))
        screen.draw.line((x, y-5), (x, y-15), (0, 0, 0))

    for i in range(3):
        x = randint(400, 540)
        y = randint(60, 200)
        screen.draw.filled_circle((x, y), 10, (255, 255, 0))
        screen.draw.line((x, y-5), (x, y-15), (0, 0, 0))

"""
dog = Actor("dog", (100, 100))

def draw():
    screen.fill("white")
    #screen.blit(images.dog, (120, 200))
    dog.draw()
    animate(dog, pos=(300, 300))
"""


"""
flg = False

x1 = 320
y1 = 240
speed1 = 5

x2 = 320
y2 = 240
speed2 = 5
"""

"""
def draw():
    screen.fill("white")
    screen.draw.filled_circle((x1, y1), 10, "red")
    screen.draw.filled_circle((x2, y2), 10, "blue")
"""

"""
def update():
    global x1, y1, speed1
    global x2, y2, speed2

    if flg:
        x1 = x1 + speed1
        if x1 >= WIDTH or x1 <= 0:
            speed1 = speed1 * -1

        y2 = y2 + speed2
        if y2 >= HEIGHT or y2 <= 0:
            speed2 = speed2 * -1

def on_key_down(key):
    global flg
    if key == keys.SPACE:
        flg = True
"""

"""
def update():
    global x, y, speed
    x = x + speed

    if x >= WIDTH or x <= 0:
        speed = speed * -1
"""

"""
# 60fps�ōX�V
def update():
    global x, y
    x = x + 1
"""

"""
def draw():
    # �w�i�F�����̃X�N���[��
    screen.fill("white")

    # �n�_(50, 50)����I�_(200, 50)�ɍ��F�̒�����`��
    screen.draw.line((50, 50), (200, 50), "black")

    # ����̍��W(50, 150)�C��100�C����100�̐ԐF�̐����`��`��
    screen.draw.rect(Rect((50, 150), (100, 100)), "red")

    # ����̍��W(50, 300)�C��100�C����100�C�ΐF�̓h��Ԃ��̐����`��`��
    screen.draw.filled_rect(Rect((50, 300), (100, 100)), "green")

    # ���S(300, 150)�C���a50�C�F�̐����`��`��
    screen.draw.circle((300, 150), 50, "blue")

    # ���S(300, 300)�C���a50�C���F�̓h��Ԃ��̐����`��`��
    screen.draw.filled_circle((300, 300), 50, "yellow")

    # ����̍��W(400, 150)�C�t�H���g�T�C�Y24�C���F�̕�����uABC�v��`��
    #screen.draw.text("ABC", (400, 150), color="black")

    # ����̍��W(400, 300)�C�t�H���g�T�C�Y32�C���F�̕�����u�������v��`��
    # IPAex�t�H���g https://moji.or.jp/ipafont/
    #screen.draw.text("������", (400, 300), fontname="ipaexg", color="black", fontsize=32)
"""
