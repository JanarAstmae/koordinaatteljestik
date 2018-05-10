from turtle import *
from easygui import *

speed(0)
delay(0)



left(180)
up()
fd(1000)
right(180)
down()
"""
Defineerin koodi, mis oskab joonistada teljestiku
"""
def joonista_teljestik ():
    for i in range(50):
        fd(10)
        lt(90)
        fd(10)    
        lt(180)
        fd(20)
        lt(180)
        fd(10)
        lt(180)
        lt(90)
        fd(10)
    lt(90)
    for i in range(50):

        fd(10)
        lt(90)
        fd(10)    
        lt(180)
        fd(20)
        lt(180)
        fd(10)
        lt(180)
        lt(90)
        fd(10)
    lt(90)
 
    lt(90)
    up()
    fd(1000)
    down()

    for i in range(50):
        fd(10)
        lt(90)
        fd(10)    
        lt(180)
        fd(20)
        lt(180)
        fd(10)
        lt(180)
        lt(90)
        fd(10)
    lt(180)
    up()
    fd(1000)
    down()

    right(90)
    for i in range(50):

        fd(10)
        lt(90)
        fd(10)    
        lt(180)
        fd(20)
        lt(180)
        fd(10)
        lt(180)
        lt(90)
        fd(10)
# Kutsun funktsiooni välja
joonista_teljestik()
y = enterbox("Sisesta funktsioon ilma '=' ja 'y'. Tundmatut tähistab x").lower()

# Alustan graafiku joonistamist
"""
Edasine kood joonistab graafiku
"""
up()
goto(-500,-500)
down()
for x in range(-500,500):
  goto(x,eval(y))
