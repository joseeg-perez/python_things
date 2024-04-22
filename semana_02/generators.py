def numeros_fibonacci(max: int) -> int:
    x = 0
    y = 1

    for _ in range(max): 
        z = x + y
        x = y
        y = z

        yield y
        
for i in (numeros_fibonacci(10)):
    print(i)