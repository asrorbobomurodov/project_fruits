def get_cheapest_fruit(data: str) -> str:
    """
    This function returns the name of the cheapest fruit

    args:
        data: CSV file with the fruits data
    returns:
        str: name of the cheapest fruit
    """
    rows = f.split("\n")
    prices = []
    name = ""
    for row in rows[1:-1]:
        item = row.split(',')
        price = float(item[-1])
        prices.append(price)
    mn = min(prices)
    
    for row in rows[1:-1]:
        item = row.split(",")
        price = float(item[-1])
        if mn == price:
            name = item[0]
    return name
    # your code here
    
f = open('fruits.csv').read()
print(get_cheapest_fruit(f))