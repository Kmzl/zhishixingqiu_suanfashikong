import time
NUM = 35
def Fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return Fibonacci(n -1) + Fibonacci(n - 2)

print("test Fibonacci")
start = time.clock()
#print(Fibonacci(NUM))
print(time.clock()-start)


#####################################
def Fibonacci_1(n):
    if n == 0 or n == 1:
        return (1, 0)
    pair = Fibonacci_1(n-1)
    return (pair[0] + pair[1], pair[0])

print("test Fibonacci_1")
start = time.clock()
fibonacci_pair = Fibonacci_1(NUM)
fibonacci_1 = fibonacci_pair[0] + fibonacci_pair[1]
print(fibonacci_1)
print(time.clock()-start)


#####################################
fibonacciSequence = []
def Fibonacci_2(n):
    if fibonacciSequence[n] == 0:  
        if n == 0 or n == 1:
            fibonacciSequence[n] = 1
        else:
            fibonacciSequence[n] = Fibonacci_2(n - 1) + Fibonacci_2(n - 2)
            
    return fibonacciSequence[n]
    
print("test Fibonacci_2")
start = time.clock()
for i in range(0, NUM + 1):
    fibonacciSequence.append(0)
print(Fibonacci_2(NUM))
print(time.clock()-start)


#####################################
def Fibonacci_3(n):
    if n == 0 or n == 1:
        return 1
    n1 = 1
    n2 = 1
    for i in range(2, n):
        tmp = n1 + n2
        n1 = n2
        n2 = tmp
    return n1 + n2

print("test Fibonacci_3")
start = time.clock()
print(Fibonacci_3(NUM))
print(time.clock()-start)
