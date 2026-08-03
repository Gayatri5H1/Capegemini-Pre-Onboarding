if __name__ == '__main__':
    N = int(input())
    lst = []
    for _ in range(N):
        c = input().split()
        if c[0] == "insert":
            lst.insert(int(c[1]), int(c[2]))
        elif c[0] == "print":
            print(lst)
        elif c[0] == "remove":
            lst.remove(int(c[1]))
        elif c[0] == "append":
            lst.append(int(c[1]))
        elif c[0] == "sort":
            lst.sort()
        elif c[0] == "pop":
            lst.pop()
        elif c[0] == "reverse":
            lst.reverse()
