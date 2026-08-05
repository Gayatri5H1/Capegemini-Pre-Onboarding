cube = lambda x: x**3

def fibonacci(n):
    # return a list of fibonacci numbers
    if n==0:
        return []
    a,b = 0,1
    res = []
    for _ in range(n):
        res.append(a)
        a,b = b, a+b
    return res

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
