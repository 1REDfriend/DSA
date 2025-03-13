import json

def convert_key(data):
    result = {int(k): v for k, v in data.items()}
    return dict(sorted(result.items(), reverse=True))

def coinExchange(total, denominations):
    if total == 0:
        output = {denom: 0 for denom in denominations.keys()}

    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    coin_combo = [{} for _ in range(total + 1)]
    coin_combo[0] = {denom: 0 for denom in denominations.keys()}

    for curr_amount in range(1, total + 1):
        for value, limit in denominations.items():
            if value <= curr_amount and min_coins[curr_amount - value] != float('inf'):
                current_usage = coin_combo[curr_amount - value].get(value, 0)
                if current_usage < limit:
                    new_total = min_coins[curr_amount - value] + 1
                    if new_total < min_coins[curr_amount]:
                        min_coins[curr_amount] = new_total
                        coin_combo[curr_amount] = coin_combo[curr_amount - value].copy()
                        coin_combo[curr_amount][value] = current_usage + 1

    if min_coins[total] == float('inf'):
        output = "Can not exchange."
    else:
        output = coin_combo[total]

    print("Amount: {}".format(total))
    if output == "Can not exchange.":
        print(output)
    else:
        print("Coin exchange result:")
        coin_count = 0
        for denom in sorted(denominations.keys(), reverse=True):
            qty = output.get(denom, 0)
            coin_count += qty
            print("  {} baht = {} coins".format(denom, qty))
        print("Number of coins: {}".format(coin_count))

def main():
    amount = int(input())
    coinList = convert_key(json.loads(input()))
    coinExchange(amount, coinList)

main()