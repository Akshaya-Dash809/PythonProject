# Function to print Fibonacci series
def fibonacci(n):
    fib_seq =[]
    a,b=0,1
    for i in range(n):
        fib_seq.append(a)
        a,b=b,a+b
    return fib_seq

numx_of_seq = int(input("Enter the number of fibonacci sequence: "))
print(fibonacci(numx_of_seq))