tea_prices_inr = {
    "Masala chai": 40,
    "Green Tea": 50,
    "Lemon tea": 200
}

tea_prices_usd = {tea: round(price / 95, 2) for tea, price in tea_prices_inr.items()}
print(tea_prices_usd)