text1 = input().strip()
text2 = input().strip()

number = len(text1)
assert len(text2) == number

dp_table = [0] * number
max_len = 0
start_index = -1

for i in range(number):
    prev = 0
    for j in range(number):
        if text1[i] == text2[j]:
            new_value = prev + 1
            if new_value > max_len:
                max_len = new_value
                start_index = i - max_len + 1
        else:
            new_value = 0
        prev = dp_table[j]
        dp_table[j] = new_value

if max_len == 0:
    print("No common substring.")
else:
    print(text1[start_index : start_index + max_len])
    print(max_len)