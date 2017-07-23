name = "Fibonacci"
# Fibonacci numbers module
def fib(n):
    a, b = 0, 1
    while b < n:
        print(b, end='  ')
        a, b = b, a+b
    print()

def fib2(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
    print("This program is being run by itself")
else:
    print("I am imported from another module")
