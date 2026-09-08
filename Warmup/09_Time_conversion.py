def time_conversion(s):
    period = s[-2:]
    hour = int(s[:2])
    min_sec = s[2:-2]

    if period == "AM":
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour += 12

    return f"{hour:02d}{min_sec}"

if __name__ == '__main__':
    s = input()
    print(time_conversion(s))