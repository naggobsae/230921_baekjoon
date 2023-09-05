while True:
    try:
        string = input()
        
        res = [0, 0, 0, 0]
        for i in string:
            if i.islower():
                res[0] += 1
            elif i.isupper():
                res[1] += 1
            elif i.isnumeric():
                res[2] += 1
            elif i.isspace():
                res[3] += 1
        print(*res)
    except EOFError:
        break
