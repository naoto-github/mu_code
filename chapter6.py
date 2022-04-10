# Turtleグラフィックスのライブラリをインポート
from turtle import *
from random import *

"""
def mouse_event(x, y):
    penup()
    goto(x, y)
    pendown()
    dot(10)
    penup()

 # マウスの左ボタン
onscreenclick(mouse_event)
"""

"""
def mouse_left(x, y):
    penup()
    goto(x, y)
    pendown()
    color("red")
    dot(10)

def mouse_center(x, y):
    penup()
    goto(x, y)
    pendown()
    color("blue")
    dot(10)

# マウスの左ボタン
onscreenclick(mouse_left, 1)

# マウスの右ボタン（トラックパッドの場合は2本指でタップ）
onscreenclick(mouse_center, 2)
"""

"""
def right():
    setheading(0)
    forward(20)

def up():
    setheading(90)
    forward(20)

def left():
    setheading(180)
    forward(20)

def down():
    setheading(270)
    forward(20)

def reset():
    resetscreen()

onkeypress(right, "Right")
onkeypress(up, "Up")
onkeypress(left, "Left")
onkeypress(down, "Down")
onkeypress(reset, "r")
listen()
"""

"""
def random_move():
    angle = randint(0, 359) # ランダムに角度を設定
    setheading(angle)
    forward(100)

ontimer(random_move, 2000) # 2000ms後に実行
"""

# ターゲットの座標
target_x = 0
target_y = 0

# タートルの速度
speed = 20

# ターゲットの更新
def setTarget(x, y):
    global target_x, target_y # グローバル変数
    global speed
    target_x = x
    target_y = y
    speed = 20

onscreenclick(setTarget)

# ターゲットを追いかける
def chase():
    global target_x, target_y # グローバル変数
    global speed
    # ターゲットまでの距離が20より大きいとき
    if(distance(target_x, target_y) > speed):
        angle = towards(target_x, target_y) # 目的方向の角度を算出
        setheading(angle)
        speed = speed + 10
        forward(speed)
    else:
        setposition(target_x, target_y)

    ontimer(chase, 200) # 200msごとにchase()を呼び出す

chase()
