a= []

while True:
    try:
        a.append(input())
    except:
        break

for i in range(len(a)):
    for s in special_char:
        a[i].replace(s, "")

    print(a[i])


