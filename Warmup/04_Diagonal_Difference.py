def diagonalDifference(arr):
    n = len(arr)
    primary_diagonal = sum(arr[i][i] for i in range(n))
    secondary_diagonal = sum(arr[i][n-1-i] for i in range(n))
    return abs(primary_diagonal - secondary_diagonal)
if __name__ == '__main__':
    n = int(input().strip())
    arr = [list(map(int, input().strip().split())) for _ in range(n)]
    result = diagonalDifference(arr)
    print(result)