import string
def print_rangoli(size):
    a = string.ascii_lowercase
    w = 4*size-3
    for i in range(size-1,0,-1):
        s = "-".join(a[size-1:i:-1] + a[i:size])
        print(s.center(w,"-"))
    for i in range(size):
        s = "-".join(a[size-1:i:-1] + a[i:size])
        print(s.center(w,"-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
