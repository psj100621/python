from cs1robots import *
load_world('venv/worlds/add34.wld')
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

def drop_beeper_N_times(X):
    for i in range(X):
        hubo.drop_beeper()
oneline()

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
hubo.move()
