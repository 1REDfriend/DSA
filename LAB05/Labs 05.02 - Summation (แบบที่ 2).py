number_str = input().strip()
count_zero = number_str.count('0')
result = 0

if number_str.startswith('-'):
    number_str = number_str[1:]

if count_zero == 0 or not number_str.startswith("10"):
    for i in range(1,int(number_str)+1) :
        result += i
else:
    result = "5" + ((count_zero - 1) * "0")
    result += result

print(result)
