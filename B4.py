import turtle as t
import math as m
a, b = map(float, input().split()) # a = 밑변, c = 높이

c = (a**2+b**2)**0.5

first_angle = m.acos((a**2+b**2-c**2)/(2*a*b))
second_angle = m.acos((b**2+c**2-a**2)/(2*b*c))
# print(180 - m.degrees(first_angle))
t.fd(a)
t.right(180 - m.degrees(first_angle))
t.fd(b)
t.right(180 - m.degrees(second_angle))
t.fd(c)

t.exitonclick()


