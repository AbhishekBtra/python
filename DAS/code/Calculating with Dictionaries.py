prices = {
    'HUL':2000,
    'Infosys':1600,
    'TCS':2400,
    'Wipro':650
}

max_prices = max(zip(prices.values(),prices.keys())) # (2400, 'TCS')

min_prices = min(zip(prices.values(),prices.keys())) # (650, 'Wipro')

sorted_prices = sorted(zip(prices.values(),prices.keys()),reverse=True) 

print(max_prices) # 2400
print(min_prices) #650 
print(sorted_prices) # [(2400, 'TCS'), (2000, 'HUL'), (1600, 'Infosys'), (650, 'Wipro')]
