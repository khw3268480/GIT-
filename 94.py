
special_char = '''"'!#$%&‚()*+,-./:;<=>?@[`\]^_„{|}~''' 

while True:
    try:
        a = input()
        for i in special_char:
            a = a.replace(i, "")
            a = a.lower()
        print(a)
    except:
        break


