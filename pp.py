def pattern(n):
    for i in range(0,n):
        for j in range(1,i+2):
            print(j, end="")
        print()    
    for i in range(n, 0, -1):
        for j in range(i-1, 0, -1):
            print(j, end="")
        print()
pattern(10)
