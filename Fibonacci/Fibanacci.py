import time
NUM = 35

##################################
def Fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return Fibonacci(n -1) + Fibonacci(n - 2)

print("test Fibonacci")
start = time.clock()
print(Fibonacci(NUM))
print(time.clock()-start)


#####################################
def Fibonacci_1(n):
    if n == 1 or n == 2:
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
        if n == 1 or n == 2:
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
    if n == 1 or n == 2:
        return 1
    n1 = 1
    n2 = 1
    for i in range(3, n):
        tmp = n1 + n2
        n1 = n2
        n2 = tmp
    return n1 + n2

print("test Fibonacci_3")
start = time.clock()
print(Fibonacci_3(NUM))
print(time.clock()-start)


#####################################
######## matrix #####################
#####################################
####### [0 1] #######################
####### [2 3] #######################
def matrix4And4Multiplication(matrix1, matrix2):
    ### [0 1] * [0 1] ##
    ### [2 3]   [2 3] ##
    result = []
    result.append(matrix1[0] * matrix2[0] + matrix1[1] * matrix2[2])
    result.append(matrix1[0] * matrix2[1] + matrix1[1] * matrix2[3])
    result.append(matrix1[2] * matrix2[0] + matrix1[3] * matrix2[2])
    result.append(matrix1[2] * matrix2[1] + matrix1[3] * matrix2[3])
    return result
    result.append(matrix1[0] * matrix2[0] + matrix1[1] * matrix2[2])
    result.append(matrix1[0] * matrix2[1] + matrix1[1] * matrix2[3])
def matrix4And2Multiplication(matrix1, matrix2):
    ### [0 1] * [0] ##
    ### [2 3] * [1] ##
    result = []
    result.append(matrix1[0] * matrix2[0] + matrix1[1] * matrix2[1])
    result.append(matrix1[2] * matrix2[0] + matrix1[3] * matrix2[1])
    return result

def matrixPower(matrix, exponent):
    matrixTmp = matrix
    for i in range(1,exponent):
        matrixTmp = matrix4And4Multiplication(matrixTmp, matrix)
    return matrixTmp
    
def Fibonacci_4(n):
    if n == 0 or n == 1:
        return [1,1,1,0]
    else:
        return matrix4And2Multiplication(matrixPower([1,1,1,0], n), [1,0])

print("test Fibonacci_4")
start = time.clock()
print(Fibonacci_4(NUM)[1])
print(time.clock()-start)


def Fibonacci_5(n):
    if n == 0 or n == 1:
        return [1,1,1,0]
    if n % 2 == 0:
        return matrix4And4Multiplication(Fibonacci_5(n/2),Fibonacci_5(n/2))
    else:
        return matrix4And4Multiplication( \
            matrix4And4Multiplication(Fibonacci_5(int(n/2)), \
                                      Fibonacci_5(int(n/2))), [1,1,1,0])
## 结果为[Fn+1  Fn  ] ##
##       [Fn,   Fn-1] ##
print("test Fibonacci_5")
start = time.clock()
print(Fibonacci_5(NUM)[1])
print(time.clock()-start)


def Fibonacci_6(n):
    if n == 0:
        return [1, 0]
    tmp = Fibonacci_6(int(n/2))
    if n % 2 == 0:
        return [tmp[0]*tmp[0] + tmp[1]*tmp[1], (2 * tmp[0] - tmp[1]) * tmp[1]]
    else:
        return [(2 * tmp[1] + tmp[0]) * tmp[0], tmp[0]*tmp[0] + tmp[1]*tmp[1]]

print("test Fibonacci_6")
start = time.clock()
print(Fibonacci_6(NUM)[1])
print(time.clock()-start)
        
