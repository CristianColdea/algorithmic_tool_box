# Uses python2
import sys

def get_change(m):
    coins_storage = []
    coins = [1, 3, 4]
    coins_storage.append(0)
    for amount in range(1,m + 1):
        NumCoins = 10 ** 4
        for coin in coins:
            if amount >= coin:
                current_coins = coins_storage[amount - coin] + 1
                if current_coins < NumCoins:
                    NumCoins = current_coins
        coins_storage.append(NumCoins)
    return NumCoins

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
