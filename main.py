'''Орнамент'''
import turtle as t
t.speed(100)

def triangle(a, b, c):

    t.fillcolor(c)
    t.down()
    t.begin_fill()
    t.right(45)
    t.fd(a)
    t.right(90)
    t.fd(a)
    t.right(135)
    t.fd(b)
    t.end_fill()
    t.up()
    t.right(90)
    t.fd(100)


def square(c,a):
    t.fillcolor(c)
    t.down()
    t.begin_fill()
    for i in range(4):
        t.fd(a)
        t.right(90)
    t.end_fill()
    t.up()


def triangle_2(a, b, c):

    t.fillcolor(c)
    t.down()
    t.begin_fill()
    t.right(45)
    t.fd(a)
    t.right(90)
    t.fd(a)
    t.right(135)
    t.fd(b)
    t.end_fill()
    t.up()
    t.fd(100)
    t.right(90)


def flouwer(c):

    t.fillcolor(c)
    t.down()
    t.begin_fill()
    for i in range(6):
        t.circle(50, 180)
        t.left(90)
    t.end_fill()
    t.up()
    t.left(90)
    t.fd(100)
    t.left(90)

def krug(c):

    t.fillcolor(c)
    t.down()
    t.begin_fill()
    t.circle(-10)
    t.end_fill()
    t.up()
    t.fd(100)

def star(c):

    t.fillcolor(c)
    t.down()
    t.begin_fill()
    for i in range(4):
        t.circle(20, 90)
        t.right(180)
    t.end_fill()
    t.up()
    t.fd(100)

t.up()
t.goto(-250, 150)
t.down()
t.fillcolor('#e14b23')
t.begin_fill()
for i in range(2):
  t.fd(500)
  t.right(90)
  t.fd(100)
  t.right(90)
t.end_fill()
t.up()

triangle(100 / (2 ** 0.5), 100, '#699031')
triangle(100 / (2 ** 0.5), 100, '#699031')
triangle(100 / (2 ** 0.5), 100, '#699031')
triangle(100 / (2 ** 0.5), 100, '#699031')
triangle(100 / (2 ** 0.5), 100, '#699031')
t.right(90)
t.fd(100)
t.right(90)
triangle(100 / (2 ** 0.5), 100, '#699031')
triangle(100 / (2 ** 0.5), 100, '#699031')
triangle(100 / (2 ** 0.5), 100, '#699031')
triangle(100 / (2 ** 0.5), 100, '#699031')
triangle(100 / (2 ** 0.5), 100, '#699031')
t.right(90)
t.fd(50)
t.right(45)

square('#435b3a', 100 / (2 ** 0.5))
t.right(45)
t.fd(100)
t.left(45)
square('#435b3a', 100 / (2 ** 0.5))
t.right(45)
t.fd(100)
t.left(45)
square('#435b3a', 100 / (2 ** 0.5))
t.right(45)
t.fd(100)
t.left(45)
square('#435b3a', 100 / (2 ** 0.5))
t.right(45)
t.fd(100)
t.left(45)
square('#435b3a', 100 / (2 ** 0.5))
t.right(45)
t.fd(10)
t.left(90)

triangle_2(80 / (2 ** 0.5), 80, '#facf05')
triangle_2(80 / (2 ** 0.5), 80, '#facf05')
triangle_2(80 / (2 ** 0.5), 80, '#facf05')
triangle_2(80 / (2 ** 0.5), 80, '#facf05')
triangle_2(80 / (2 ** 0.5), 80, '#facf05')
t.left(90)
t.bk(180)
t.left(90)
triangle_2(80 / (2 ** 0.5), 80, '#facf05')
triangle_2(80 / (2 ** 0.5), 80, '#facf05')
triangle_2(80 / (2 ** 0.5), 80, '#facf05')
triangle_2(80 / (2 ** 0.5), 80, '#facf05')
triangle_2(80 / (2 ** 0.5), 80, '#facf05')


t.goto(-250, 150)
t.fd(200)
t.left(90)
t.down()
t.fillcolor('#E6E6FA')
t.begin_fill()
for i in range(2):
  t.fd(500)
  t.right(90)
  t.fd(100)
  t.right(90)
t.end_fill()
t.up()

t.right(90)
t.fd(100)
t.left(90)
flouwer('#8882be')
flouwer('#8882be')
flouwer('#8882be')
flouwer('#8882be')
flouwer('#8882be')

t.goto(-250, -90)
t.fd(50)
krug('#483D8B')
krug('#483D8B')
krug('#483D8B')
krug('#483D8B')
krug('#483D8B')

t.goto(-170, -100)
star('#FFC0CB')
star('#FFC0CB')
star('#FFC0CB')
star('#FFC0CB')

t.fd(100)

t.mainloop()
