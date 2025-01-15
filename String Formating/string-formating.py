def printformat(n):
    l=len(bin(n)[2:])
    for i in range (1, n+1):
        print(str(n).rjust(l), oct(i)[2:].rjust(l), hex(i)[2:].upper().rjust(l), bin(i)[2:].rjust(l))

number = int(input())
printformat(number)
