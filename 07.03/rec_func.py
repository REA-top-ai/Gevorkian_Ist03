def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def factorial2(n):
    if n == 0:
        return 1
    else:
        for i in range(n - 1 , 0 , - 1):
            n *= i
    return n

print(factorial(10))
print(factorial2(10))

def square_list(list):
    for i in range (len(list)):
        list[i] = int(list[i])**2
    return list

print(square_list(['1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9']))

