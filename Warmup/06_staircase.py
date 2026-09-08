def staircase(n):
    for i in range(1, n+1):
        print(" " * (n-i) + "#" * i)
        # print("#" * (n-i) + " " * i)  //for revrese staircase

if __name__ == '__main__':
    n = int(input())
    staircase(n)