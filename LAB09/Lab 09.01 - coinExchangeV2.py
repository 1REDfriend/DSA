import json

def convert_key(data):
    result = {int(k): v for k, v in data.items()}
    return dict(sorted(result.items(), reverse=True))

def coinExchange(amount, coinList, duplexNum = 1):
    original_amount = amount
    find_coin_remaining = 0
    isMaximum_duplex = False
    result = {x: 0 for x,_ in coinList.items()}
    coin_values = [x for x,_ in coinList.items()]

    # หาจำนวนเหรียญที่ต้องใช้ในแต่ละเหรียญ
    for coin_value in coin_values:
        num_coins = min(amount // coin_value, coinList[coin_value])
        result[coin_value] = num_coins
        amount -= num_coins * coin_value
        canExchange = False
        for coin_key in coin_values :
            if coinList[coin_key] <= 0 :
                continue
            if amount >= coin_key :
                canExchange = True
        if not canExchange and amount > 0 :
            result[coin_value] = result[coin_value] - duplexNum
            amount += coin_value
            if result[coin_value] - duplexNum <= 0 :
                isMaximum_duplex = True
    for v in coinList.values() :
        find_coin_remaining += v
    if amount > 0 and find_coin_remaining > 0 and not isMaximum_duplex:
        coinExchange(original_amount, coinList, duplexNum + 1)

    print(f"Amount: {original_amount}")
    if amount > 0:
        print("Coins are not enough.")
    else:
        print("Coin exchange result:")
        for coin_value in coin_values:
            print(f"  {coin_value} baht = {result[coin_value]} coins")
        total_coins = sum(result.values())
        print(f"Number of coins: {total_coins}")

def main():
    amount = int(input())
    coinList = convert_key(json.loads(input()))
    coinExchange(amount, coinList)

main()