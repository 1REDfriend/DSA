def calculator(n):
    if n == 1:
        return 1

    total_digits = sum(len(str(i)) for i in range(1, n+1))

    return total_digits + n

print(calculator(int(input().strip())))