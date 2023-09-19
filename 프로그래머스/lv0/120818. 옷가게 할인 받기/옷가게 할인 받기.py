def solution(price):
    if price >= 500000:
        return int(price-price*0.2)
    elif 500000 > price >= 300000:
        return int(price-price*0.1)
    elif 300000 > price >= 100000:
        return int(price-price*0.05)
    else:
        return price