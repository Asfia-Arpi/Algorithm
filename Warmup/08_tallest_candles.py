# def birthdayCakeCandles(candles):
#     tallest = max (candles)
#     count = 0
#     for height in candles:
#         if height == tallest:
#             count += 1
#     return count
# if __name__ =='__main__':
#     candles = list(map(int,input().split()))
#     print(birthdayCakeCandles(candles))

def birthdayCakeCandles(candles):
    tallest = max (candles)
    count = candles.count(tallest)
    return count
if __name__ == '__main__':
    n = int(input())
    candles = list(map(int,input().split()))
    print(birthdayCakeCandles(candles))