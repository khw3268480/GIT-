import turtle as t

length = int(input())
house = int(input())


def home(length, house, t):
    for i in range(house):
        t.left(60)
        t.fd(length)
        t.right(120)
        t.fd(length)
        t.right(120)
        t.fd(length)
        t.left(90)
        t.fd(length)
        t.left(90)
        t.fd(length)
        t.left(90)
        t.fd(length)
        t.right(90)
home(length, house, t)
t.exitonclick()