x = eval(input("input x:"))
while(x > 1):
    if(x % 2) == 0:
        print(x)
        x = x/2
    else:
        print(x)
        x = 3 * x + 1
print(x)
