import turtle as t
width, height = map(int, input().split())
step_count = int(input())

def steps(t, width, height, step_count):
    for i in range(step_count):
        t.left(90)
        t.fd(height)
        t.left(270)
        t.fd(width)

steps(t, width, height, step_count)