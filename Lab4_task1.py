from cs1robots import *
load_world('worlds/add34.wld')
hubo = Robot()
hubo.set_trace('blue')

def turnright():
    for i in range(3):
        hubo.turn_left()


def oneline():
    while hubo.front_is_clear():
        hubo.move()

def pick_all_beeper():
    num = 0
    while hubo.on_beeper():
        hubo.pick_beeper()
        num = num +1
    return num

def quotient(x,y):
    return (x+y) // 10

def remainder(x,y):
    return (x+y) % 10

def sum(x,y):
    return (x+y)

def drop_beeper_N_times(X):
    for i in range(X):
        hubo.drop_beeper()
def addition():
    x = pick_all_beeper()
    hubo.turn_left()
    hubo.move()
    y = pick_all_beeper()
    r = remainder(x,y)
    q = quotient(x,y)
    for i in range(2):
        hubo.turn_left()
    hubo.move()
    drop_beeper_N_times(r)
    for i in range(2):
        hubo.turn_left()
    for i in range(2):
        hubo.move()
    hubo.turn_left()
    hubo.move()
    drop_beeper_N_times(q)
    for i in range(4):
        hubo.move()
        hubo.turn_left()
    hubo.turn_left()
    a = pick_all_beeper()
    hubo.move()
    b = pick_all_beeper()
    c = sum(a,b)
    hubo.move()
    drop_beeper_N_times(c)
    turnright()
    hubo.move()
    hubo.turn_left()
    hubo.turn_left()
    x = 0
    y = 0
    r = 0
    q = 0
    a = 0
    b = 0
    c = 0

oneline()
for i in range(2):
    addition()