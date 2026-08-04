def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        t = ""
        for c in string[i:i+k]:
            if c not in t:
                t += c
        print(t)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
