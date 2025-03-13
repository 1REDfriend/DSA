from collections import defaultdict

text1 = input().strip()
text2 = input().strip()

number = len(text1)
assert len(text2) == number

char_positions = defaultdict(list)
for j, char in enumerate(text2):
    char_positions[char].append(j)

dp_table = [0] * number
max_len = 0
start_index = -1

if text1[0] in char_positions:
    for j in char_positions[text1[0]]:
        dp_table[j] = 1
        if 1 > max_len:
            max_len = 1
            start_index = 0

for i in range(1, number):
    char = text1[i]
    if char not in char_positions:
        dp_table = [0] * number
        continue
    positions = char_positions[char]
    temp_table = dp_table.copy()

    dp_table = [0] * number

    for j in positions:
        if j == 0:
            new_value = 1
        else:
            new_value = temp_table[j - 1] + 1
        dp_table[j] = new_value
        if new_value > max_len:
            max_len = new_value
            start_index = i - max_len + 1

if max_len == 0:
    print("No common substring.")
else:
    print(text1[start_index:start_index + max_len])
    print(max_len)