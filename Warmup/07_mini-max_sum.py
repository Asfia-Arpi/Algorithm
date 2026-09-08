def min_max(arr):
    min_val = arr[0]
    max_val = arr[0]
    total_sum = 0
    for num in arr:
        total_sum += num
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
            
    min_sum = total_sum - max_val
    max_sum = total_sum - min_val
    
    print(min_sum, max_sum)


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    min_max(arr) 