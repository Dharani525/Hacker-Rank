

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    counted = 0
    matched = set(ar)
    for i in matched:
        counted += ar.count(i)//2
    return counted            


n = int(input())

ar = list(map(int, input().rstrip().split()))

print(sockMerchant(n, ar))

