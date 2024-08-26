n = int(input())
serials = [input().strip() for _ in range(n)]

def sum_of_numbers(serial):
    digit_sum = 0
    for char in serial:
        if char.isdigit():
            digit_sum += int(char)
    return digit_sum

def serial_key(serial):
    return (len(serial), sum_of_numbers(serial), serial)

serials_sorted = sorted(serials, key=serial_key)

for serial in serials_sorted:
    print(serial)