strs = []
special_char = '''1234567890"'!#$%&‚()*+,-./:;<=>?@[\]^_„{|}~`''' 

while True:
    try:
        a = input()
        for i in special_char:
            a = a.replace(i, " ")
        a = a.lower()
        strs.append(a.split())
    except:
        break

result = sum(strs, [])
result = list(set(result))
result.sort()
for p in result:
    print(p)