import requests


def get_solana_price():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "solana",
        "vs_currencies": "usd"
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        sol_price = data["solana"]["usd"]
        return sol_price
    else:
        return None


# 调用函数获取Solana代币价格
sol_price = get_solana_price()
if sol_price:
    print(f"The current price of Solana (SOL) is ${sol_price}")
else:
    print("Failed to retrieve Solana price. Please try again later.")
