name = []
score = []
while True:
    try:
        t = input().split()
        name.append(t[0])
        score.append(sum(int(t[1:len(t)])))
    except:
        break

print(name, score)