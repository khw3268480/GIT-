a = []

while True:
    try:
        a.append(float(input()))
    except:
        break

a.sort(reverse=True)

print(f"{a[0]:.1f} {a[1]:.1f} {a[2]:.1f}")