def minion_game(string):
    # your code goes here
    v = "AEIOU"
    k = 0
    st = 0
    n = len(string)
    for i in range(n):
        if string[i] in v:
            k += n-i
        else:
            st += n-i 
    if k > st:
        print("Kevin", k)
    elif st > k:
        print("Stuart", st)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
