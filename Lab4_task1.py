from cs1robots import *
load_world('worlds/add5.wld')
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

def quotient(x,y,z):
    return (x+y+z) // 10

def remainder(x,y,z):
    return (x+y+z) % 10

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
    hubo.move()
    z = pick_all_beeper()
    r = remainder(x,y,z)
    q = quotient(x,y,z)
    for i in range(2):
        hubo.turn_left()
    for i in range(2):
        hubo.move()
    drop_beeper_N_times(r)
    for i in range(2):
        hubo.turn_left()
    for i in range(2):
        hubo.move()
    hubo.turn_left()
    hubo.move()
    drop_beeper_N_times(q)
    hubo.turn_left()
    hubo.move()
    hubo.move()
    hubo.turn_left()

oneline()
for i in range(5):
    addition()