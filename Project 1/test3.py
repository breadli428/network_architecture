def prof(n):
    lr = [0, 10, 20, 40, 60, 100]
    rat = [1, 0.1, 0.075, 0.05, 0.03, 0.01]
    sum1 = 0
    for ind in range(6):
        if lr[ind] <= n:
            sum1 = sum1 + lr[ind] * rat[ind]
        else:
            sum1 = sum1 + (n - lr[ind-1]) * rat[ind]
            break
    return sum1


i = int(input('li run = '))
mysum = prof(i)
print(mysum)
