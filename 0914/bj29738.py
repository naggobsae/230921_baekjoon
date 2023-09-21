t = int(input())

for i in range(1, t + 1):
    x = int(input())
    if x <= 25:
        print("Case #{}: World Finals".format(i))
    elif x <= 1000:
        print("Case #{}: Round 3".format(i))
    elif x <= 4500:
        print("Case #{}: Round 2".format(i))
    else:
        print("Case #{}: Round 1".format(i))