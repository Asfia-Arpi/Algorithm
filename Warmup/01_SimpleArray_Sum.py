def SimpleArraySum(ar):
    total = 0
    for num in ar:
        total += num
    return total
if __name__ == '__main__':
    n = int(input().strip())
    ar = list(map(int,input().rstrip().split()))
    result = SimpleArraySum(ar)
    print (result)