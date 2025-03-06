import json

def convert_key(data):
    return {int(k): v for k, v in data.items()}

def coinExchange(amount, coinList):
    original_amount = amount
    result = {10: 0, 5: 0, 2: 0, 1: 0}
    coin_values = [10, 5, 2, 1]

    for coin_value in coin_values:
        num_coins = min(amount // coin_value, coinList[coin_value])
        result[coin_value] = num_coins
        amount -= num_coins * coin_value

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